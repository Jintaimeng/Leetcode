using namespace std;

const intN=110;
int f[N][N];
int a[N],b[N];

int main(){
ios::sync_with_stdio(false);
int n,m,p;
cin>>n>>m>>p;
for(int i=1;i<=n;i++) cin>>a[i]>>b[i];
memset(f,-0x3f,sizeof(f));
f[1][0]=b[1];
for(int i=2;i<=n;i++){
    for(int&nbsp;j=1;j<i;j++)
        if(a[i]-a[j]<=m)
            for(int&nbsp;k=1;k<=p;k++)
                f[i][k]=max(f[i][k],f[j][k-1]+b[i]);
    }
int ans=0;//枚举最后的结果，有可能热气器次数没用完就取完了所有金币
for(int i=1;i<=n;i++)
    for(int&nbsp;j=1;j<=p;j++)
        ans=max(ans,f[i][j]);
cout<<ans<<endl;
return&nbsp;0;
}