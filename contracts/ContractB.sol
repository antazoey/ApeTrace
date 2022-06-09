// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import { Hero, ContractC } from "./ContractC.sol";


contract ContractB {

    ContractC public contractC;
    mapping(address => uint256) public bandPractice;
    mapping(address => string) public pumpkin;
    string public concatres = "";
    string public sharedString = "";
    address public sharedAddress = 0xF2Df0b975c0C9eFa2f8CA0491C2d1685104d2488;
    string public symbol = "SYMBOL";

    constructor(ContractC addr) {
        contractC = addr;
    }

    function setSharedString(string memory value) public {
        sharedString = value;
    }

    function setSharedAddress(address value) public {
        sharedAddress = value;
    }

    function methodB1(string memory lolol, uint dynamo) public {
        pumpkin[msg.sender] = lolol;
        
        // Turns out this should not be working!
        // string memory converted_lols = string(abi.encodePacked(lolol));
        // string memory result = string.concat(converted_lols, " Captain Janeway");
        // concatres = result;
        
        contractC.getSomeList();
        contractC.methodC1("simpler", dynamo, msg.sender);
        bandPractice[msg.sender] = bandPractice[msg.sender] + dynamo;
    }

    function callMe(address blue) public pure returns(address) {
        return blue;
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
