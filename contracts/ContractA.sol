// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import "./ContractB.sol";

contract ContractA {

    ContractB public contractB;
    ContractC public contractC;
    mapping(address => uint256) public runTheJules;

    constructor(ContractB addrb, ContractC addrc) {
        contractB = addrb;
        contractC = addrc;
    }

    function methodWithoutArguments() public payable {
        contractB.methodB1();
        contractB.methodB1();
        contractB.methodB2(msg.sender);
        runTheJules[address(contractC)] = contractC.addressToValue(msg.sender);
        
        // TODO: Partially fail
        //contractB.alwaysFail(9);
        
        contractB.methodB1();
        contractB.methodB1();
    }

    function methodWithSingleArgument(uint256 rtj) public payable returns(bool) {
        runTheJules[msg.sender] = rtj;
        contractB.methodB1();
        contractB.methodB2(msg.sender);
        contractB.methodB2(msg.sender);
        uint256 val = contractB.bandPractice(msg.sender);
        runTheJules[msg.sender] += val;
        return true;
    }
}
