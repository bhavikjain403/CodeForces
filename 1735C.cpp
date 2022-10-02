#include<bits/stdc++.h>
#define int long long
using namespace std;

int solve(vector<int> &arr1,int j) {
    int c=0;
    int p=j;
    while(p!=-1) {
        p=arr1[p];
        c++;
        if(p==j)
        return c;
    }
    return -1;
}

signed main() {
    int t,n;
    string s;
    cin>>t;
    while(t--) {
        cin>>n;
        cin>>s;
        vector<int> arr1(26,0);
        int arr2[26];
        for(int i=0; i<26; i++) arr1[i]=-1,arr2[i]=1;
        for(int i=0; i<n; i++) {
            if(arr1[s[i]-'a']==-1) {
                for(int j=0; j<26; j++) {
                    if(arr2[j]!=0 and j!=s[i]-'a') {
                        arr1[s[i]-'a']=j;
                        int temp=solve(arr1,j);
                        if(temp!=-1 and temp!=26)
                            continue;
                        else {
                            arr2[j]=0;
                            break;
                        }
                    }
                }
            }
            cout<<char(arr1[s[i]-'a']+'a');
        }
        cout<<endl;
    }
    return 0;
}