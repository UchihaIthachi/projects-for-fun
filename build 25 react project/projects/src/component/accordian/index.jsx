import React, { useState } from "react";
import data from "./data";
import "./styles.css";

const Accordion = () => {
    const [selected, setSelected] = useState(null);
    const [enableMultiSelect, setEnableMultiSelect] = useState(false);  
    //
    const [multiple, setMultiple] = useState([]);

    
    function handleSingleSelection(getSelectedId){
        setSelected(getSelectedId===selected?null:getSelectedId);

    }
    function handleMultiSelection(getCurrentId){
        let cpyMultiple = [...multiple];
        const indexCurrentId = cpyMultiple.indexOf(getCurrentId);
        if (indexCurrentId > -1) {
            cpyMultiple.splice(indexCurrentId, 1);
        } else {
            cpyMultiple.push(getCurrentId);
        }
        setMultiple(cpyMultiple)
    }
    
    return(
        <div className="acc-wrapper">
            <button onClick={() => setEnableMultiSelect(!enableMultiSelect)}>
                {enableMultiSelect ? "Disable Multi Selection" : "Enable Multi Selection"}
            </button>

            <div className="accordian">
            {data && data.length>0 ?(
                data.map((dataItem) =>(
                    <div className="item">
                        <div 
                        onClick={
                            enableMultiSelect
                              ? () => handleMultiSelection(dataItem.id)
                              : () => handleSingleSelection(dataItem.id)
                          }
                        className="title">
                            <h2>{dataItem.question}</h2>
                            <span>+</span>
                        </div>

                        <div>
                        {enableMultiSelect
                        ? multiple.indexOf(dataItem.id) !== -1 && (
                        <div className="acc-content ">{dataItem.answer}</div>
                        )
                        : selected === dataItem.id && (
                        <div className="acc-content ">{dataItem.answer}</div>
                        )
                        }
                        </div>
                        
                    </div>
                )
                )
            ):(
                <div>No data Found!</div>
            )}
            </div>
        </div>
    );
}

export default Accordion;
