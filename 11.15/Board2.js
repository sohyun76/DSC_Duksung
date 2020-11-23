import React, {useState} from 'react';

const IterationSample = () => {
    const[names,setNames] = useState([]);
    const [inputText, setInputText] = useState('');
    const [inputText2, setInputText2] = useState('');
    const[nextId, setNextId] = useState(1);

    const onChange = e => setInputText(e.target.value);
    const onChange2 = e => setInputText2(e.target.value);
    const onClick = () => {
        const nextNames = names.concat({
            id:nextId,
            text: inputText,
            text2: inputText2
        });
        setNextId(nextId + 1);
        setNames(nextNames);

        setInputText('');
        setInputText2('');
    };
    const namesList = names.map(name => <div key={name.id}>글 제목:{name.text}<br></br>내용:{name.text2}<br></br></div>);
    // const namesList = names.map(name => <li style={{listStyle:"none"}} key={name.id})....
    return(
        <>
        <h1>게시판</h1>
        <input placehoder="글 제목" value={inputText} onChange={onChange} ></input>
        <br></br>
        <textarea placehoder="내용" value={inputText2} onChange={onChange2}></textarea>
        <br></br>
        <button onClick={onClick}>작성하기</button>
        <ul>{namesList}</ul>
        </>
    );
    };
export default IterationSample;