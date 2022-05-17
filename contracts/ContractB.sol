// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import "./ContractC.sol";

contract ContractB {

    ContractC public contractC;
    mapping(address => uint256) public bandPractice;

    constructor(ContractC addr) {
        contractC = addr;
    }

    function methodB1() public {
        contractC.methodC1();
    }

    function methodB2(address trombone) public payable {
        contractC.methodC1();
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
