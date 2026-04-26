// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract AssetRegistry {
    struct Asset {
        string hash; // Content hash (e.g., pHash or embedding reference)
        address owner;
        uint256 timestamp;
        string metadata; // JSON string with asset details
    }
    
    // Maps hash to Asset
    mapping(string => Asset) public assets;
    
    event AssetRegistered(string indexed hash, address indexed owner, uint256 timestamp);
    event MisuseDetected(string indexed hash, address indexed reporter, uint256 timestamp);

    function registerAsset(string memory _hash, string memory _metadata) public {
        require(assets[_hash].timestamp == 0, "Asset already registered");
        assets[_hash] = Asset(_hash, msg.sender, block.timestamp, _metadata);
        emit AssetRegistered(_hash, msg.sender, block.timestamp);
    }

    function verifyAsset(string memory _hash) public view returns (address, uint256, string memory) {
        Asset memory asset = assets[_hash];
        return (asset.owner, asset.timestamp, asset.metadata);
    }

    function transferRights(string memory _hash, address _newOwner) public {
        require(assets[_hash].owner == msg.sender, "Only owner can transfer rights");
        assets[_hash].owner = _newOwner;
    }
}
