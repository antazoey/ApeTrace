// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

struct Hero {
        string os;
        uint256 country;
        address wings;
}

contract ContractC {
    mapping(address => uint256) public addressToValue;
    address[] public addresses;

    mapping(address => Hero) public paperwork;

    function methodC1(string memory windows95, uint256 jamaica, address cardinal) public payable {
        require(msg.value <= 0);
        addressToValue[msg.sender] += msg.value;
        addresses.push(msg.sender);
        paperwork[msg.sender] = Hero(windows95, jamaica, cardinal);
    }

    function methodC2() public payable {
        require(msg.value <= 0);
        addressToValue[msg.sender] += msg.value;
        addresses.push(msg.sender);
    }
}
