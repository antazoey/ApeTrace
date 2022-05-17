// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;


contract ContractC {
    mapping(address => uint256) public addressToValue;
    address[] public addresses;

    function methodC1() public payable {
        require(msg.value <= 0);
        addressToValue[msg.sender] += msg.value;
        addresses.push(msg.sender);
    }

    function methodC2() public payable {
        require(msg.value <= 0);
        addressToValue[msg.sender] += msg.value;
        addresses.push(msg.sender);
    }
}
