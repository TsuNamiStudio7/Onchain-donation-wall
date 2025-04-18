// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DonationWall {
    address public owner;

    struct Donor {
        address addr;
        uint256 amount;
    }

    Donor[] public donors;

    event DonationReceived(address indexed from, uint256 amount);

    constructor() {
        owner = msg.sender;
    }

    function donate() external payable {
        require(msg.value > 0, "Donation must be greater than zero");
        donors.push(Donor(msg.sender, msg.value));
        emit DonationReceived(msg.sender, msg.value);
    }

    function getDonors() external view returns (Donor[] memory) {
        return donors;
    }

    function withdraw() external {
        require(msg.sender == owner, "Only owner can withdraw");
        payable(owner).transfer(address(this).balance);
    }

    function getTotalDonations() external view returns (uint256) {
        return address(this).balance;
    }

    function getDonorCount() external view returns (uint256) {
        return donors.length;
    }
}
