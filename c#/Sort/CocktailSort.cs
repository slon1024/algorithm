using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Sort
{
    public class CocktailSort : ISort
    {

        public ArrayList Sort(ArrayList inArray)
        {
            int i = 0, k = inArray.Count - 1;
            while(i < k)
            {
                for(int j=i,l=k+1; j<l; j++)
                {
                    if ((int)inArray[j] < (int)inArray[i])
                        Swap(i, j, ref inArray);
                }
                for(int m=k; m>i; m--)
                {
                    if( (int)inArray[m] > (int)inArray[k] )
                        Swap(m, k, ref inArray);
                }

                i++;
                k--;
            }

            return inArray;
        }

        public void Swap(int i, int j, ref ArrayList inArray)
        {
            var tmp = inArray[j];
            inArray[j] = inArray[i];
            inArray[i] = tmp;
        }
    }
}
