int *[]left= {1,2,3,4,5,6,7,8,9};
int *[]hit= {1,2,3};
int *[]ans= {};
for (int i=0; i<10; i++)
{
     ans[i]= left[i] && !hit[i];
}
