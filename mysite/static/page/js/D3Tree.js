// 자료구조 초기화.
console.log(window.screen.availWidth)
var p = document.body.clientWidth;
p/2;
var branches = [];
var seed = {i: 0, x:p, y:600, a: 0, l: 150, d:0}; // i는 id, a는 각도, l은 길이, d는 계층
var da = 0.5; // 각도의 변화량
var dl = 0.8; // 길이의 변화량
var ar = 0.7; // 랜덤 보정 상수.
var maxDepth = 10; // 계층 제한 상수.

// 나무 만드는 함수

function branch(b){
    var end = endPt(b), daR, newB;
    branches.push(b);
    
    if (b.d == maxDepth)
        return;
    
    //왼쪽 가지
    daR = ar * Math.random() - ar * 0.5;
    newB = {
        i : branches.length,
        x: end.x,
        y: end.y,
        a: b.a - da + daR,
        l : b.l * dl,
        d : b.d + 1,
        parent: b.i
    };
    branch(newB);
    
    //오른쪽 가지
    daR = ar * Math.random() - ar * 0.5;
    newB = {
        i: branches.length, //id
        x: end.x, //x 포인트
        y: end.y, //y 포인트
        a: b.a + da + daR, // 다음으로 만들 브런치를 위한 각도.
        l: b.l * dl, // 다음으로 만들 브런치를 위한 길이.
        d: b.d + 1, // 계층 수준.
        parent: b.i
    };
    branch(newB);
}

function endPt(b){
    var x = b.x + b.l * Math.sin( b.a );
    var y = b.y - b.l * Math.cos( b.a );
    return {x: x, y: y};
}


//
//
//
//D3 function

function x1(d) {return d.x;}
function y1(d) {return d.y;}
function x2(d) {return endPt(d).x;}
function y2(d) {return endPt(d).y;}
function highlightParents(d) {
	var colour = d3.event.type === 'mouseover' ? 'green' : '#777';
	var depth = d.d;
	for(var i = 0; i <= depth; i++) {
		d3.select('#id-'+parseInt(d.i)).style('stroke', colour);
		d = branches[d.parent];
	}	
}

branch(seed);
console.log(branches)

function create(){
    d3.select('svg')
        .selectAll('line')
        .data(branches)
        .enter()
        .append('line')
        .attr('x1', x1)
        .attr('y1', y1)
        .attr('x2', x2)
        .attr('y2', y2)
        .style('stroke-width', function(d){return parseInt(maxDepth + 1 - d.d) + 'px';})
        .attr('id', function(d){return 'id-'+d.i;})
        .on('mouseover', highlightParents)
        .on('mouseout', highlightParents);
}

create();