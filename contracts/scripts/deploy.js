const hre = require("hardhat");

async function main() {
  const AssetRegistry = await hre.ethers.getContractFactory("AssetRegistry");
  const assetRegistry = await AssetRegistry.deploy();

  await assetRegistry.waitForDeployment();

  console.log("AssetRegistry deployed to:", await assetRegistry.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
