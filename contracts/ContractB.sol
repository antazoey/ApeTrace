// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import { Hero, ContractC } from "./ContractC.sol";


contract ContractB {

    ContractC public contractC;
    mapping(address => uint256) public bandPractice;
    mapping(address => string) public pumpkin;
    string public concatres = "";

    constructor(ContractC addr) {
        contractC = addr;
    }

    function methodB1(string memory lolol, uint256 dynamo) public {
        pumpkin[msg.sender] = lolol;
        
        // Turns out this should not be working!
        // string memory converted_lols = string(abi.encodePacked(lolol));
        // string memory result = string.concat(converted_lols, " Captain Janeway");
        // concatres = result;
        
        contractC.methodC1("simpler", dynamo, msg.sender);
        bandPractice[msg.sender] = bandPractice[msg.sender] + dynamo;
    }

    function methodB2(address trombone) public payable {
        (string memory os,,) = contractC.paperwork(msg.sender);
        contractC.methodC1(os, msg.value, address(contractC));
        bandPractice[trombone] = msg.value;
        contractC.methodC2();
        contractC.methodC2();
    }

    function alwaysFail(uint256 pointlessArgument) public {
        if (true) {
            revert("I always fail :)");
        }
        bandPractice[msg.sender] = 912412512412341241254;
        bandPractice[msg.sender] = pointlessArgument;
    }
}
