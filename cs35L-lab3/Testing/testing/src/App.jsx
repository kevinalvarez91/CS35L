import { useState } from 'react';

const Square = () => {
    const [value, setValue] = useState(null);
    
    function handleClick(){
	setValue("X");
    }


    
    return (<button className="square" onClick={handleClick}>{value}</button>);
}

const Output = () => {
    return console.log("Hi");
}


function Board() {


    
    
  return (
    <>
    <div className="status">Next player: X</div>
    <Output />
    <div>
    <Square />
    <Square />
    <Square />
    </div>
    <div>
    <Square />
    <Square />
    <Square />
    </div>
    <div>
    <Square />
    <Square />
    <Square />
    </div>
    



    </>
  );
}

export default function Game(){
  return (
    <div className="game">
      <div className="game-board">
        <Board />
      </div>
      <div className="game-info">
        <ol></ol>
        </div>
    </div>
  );


}


function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
