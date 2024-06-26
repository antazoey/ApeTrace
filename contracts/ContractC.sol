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

    event EventC(
        address indexed sinker,
        uint256 indexed hook
    );

    function methodC1(string memory windows95, uint256 jamaica, address cardinal) public payable {
        require(msg.value <= 0, "!money");
        addressToValue[cardinal] += msg.value;
        addresses.push(cardinal);
        paperwork[cardinal] = Hero(windows95, jamaica, cardinal);
        emit EventC(msg.sender, 3412);
    }

    function methodC2() public payable {
        require(msg.value <= 0, "!money");
        addressToValue[msg.sender] += msg.value;
        addresses.push(msg.sender);
    }

    function methodC3() public {
        
    }

    function getSomeList() public pure returns(uint128[3] memory) {
        return [
            3425311345134513461345134534531452345,
            111344445534535353,
            993453434534534534534977788884443333
        ];
    }
}
