#include <bits/stdc++.h> 


int solve(vector<int>& weight, vector<int>& value, int idx, int maxWeight){
	if(idx==0){
		if(weight[idx]<=maxWeight){
			return value[0];
		}
		else{
			return 0;
		}
	}

	int include =0; 
	if(weight[idx]<=maxWeight){
		include=value[idx]+solve(weight,value,idx-1,maxWeight-weight[idx]);
	}
	int exclude = 0;
	exclude = solve(weight,value,idx-1,maxWeight);
	int ans = max(include,exclude);
	return ans;
}


int solveMem(vector<int>& weight, vector<int>& value, int idx, int maxWeight,vector<vector<int>>& dp){
	if(idx==0){
		if(weight[idx]<=maxWeight){
			return value[0];
		}
		else{
			return 0;
		}
	}
	if(dp[idx][maxWeight]!=-1){
		return dp[idx][maxWeight];
	}

	int include =0; 
	if(weight[idx]<=maxWeight){
		include=value[idx]+solveMem(weight,value,idx-1,maxWeight-weight[idx],dp);
	}
	int exclude = 0;
	exclude = solveMem(weight,value,idx-1,maxWeight,dp);
	int ans = max(include,exclude);
	dp[idx][maxWeight]=ans;
	return ans;
}

int solveTab(vector<int>& weight, vector<int>& value, int idx, int maxWeight){
	vector<vector<int>> dp(n,vector<int>(maxWeight+1),-1);

	//Base case implementation
	for(int w=weight[0]; w<=maxWeight;w++){
		if(weight[0]<=maxWeight){
			dp[0][w]=value[0];
		}
		else{
			dp[0][w]=0;
		}

	}
	for(int index=1; index<n; index++){
		for(int w=0; w<=maxWeight; w++){
			int include =0; 
			if(weight[index]<=w){
				include=value[index]+ dp[index-1][w-weight[index]];
			}
			int exclude = 0;
			exclude = dp[index-1][w];// solveMem(weight,value,idx-1,maxWeight,dp);
			dp[index][w]= max(include,exclude);
		}
	}


	return dp[n-1][maxWeight];
}

int knapsack(vector<int> weight, vector<int> value, int n, int maxWeight) 
{
	// Write your code here
	//solve(weight,value,n-1,maxWeight);

	// vector<vector<int>> dp(n,vector<int>(maxWeight+1,-1));
	// solveMem(weight,value,n-1,maxWeight,dp);
	solve(weight,value,n-1,maxWeight);
}