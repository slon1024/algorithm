using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Sort
{
    public class StrandSort : ISort
    {

        public ArrayList Sort(ArrayList inArray)
        {
            var result = new ArrayList();
            while(inArray.Count > 0)
            {
                var subList = Loop(ref inArray);
                result = Merge(result, subList);
            }
            
            return result;
        }

        private ArrayList Merge(ArrayList left, ArrayList right)
        {
            return MergeSort.Merge(left, right);
        }


        private ArrayList Loop(ref ArrayList inArray)
        {
            var subList = new ArrayList { inArray[0] };
            inArray.RemoveAt(0);

            int i = 0;
            while( i < inArray.Count)
            {
                if ((int)inArray[i] > (int)subList[subList.Count-1])
                {
                    subList.Add(inArray[i]);
                    inArray.RemoveAt(i);
                }
                else
                    i++;
                     
            }

            return subList;
        }
    }
}
