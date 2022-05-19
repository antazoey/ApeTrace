// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import { Hero, ContractC } from "./ContractC.sol";


contract ContractB {

    ContractC public contractC;
    mapping(address => uint256) public bandPractice;
    mapping(address => bytes32) public pumpkin;

    constructor(ContractC addr) {
        contractC = addr;
    }

    function methodB1(bytes32 lolol, uint256 dynamo) public {
        pumpkin[msg.sender] = lolol;
        string memory converted_lols = string(abi.encodePacked(lolol));
        string memory result = string.concat(converted_lols, " Captain Janeway");
        contractC.methodC1(result, dynamo, msg.sender);
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
