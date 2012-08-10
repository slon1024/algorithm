using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Sort
{
    public class CombSort : ISort
    {
        
        public ArrayList Sort(ArrayList inArray)
        {
            Gap = inArray.Count;
            while(Gap>1)
            {
                Gap = Gap;
                int i = 0;

                while (i + Gap < inArray.Count)
                {
                    if ((int)inArray[i + Gap] < (int)inArray[i])
                    {
                        var tmp = inArray[i + Gap];
                        inArray[i + Gap] = inArray[i];
                        inArray[i] = tmp;
                    }
                    i++;
                }
            }
            return inArray;
        }

        private int _gap;
        public int Gap
        {
            get { return _gap; }
            set { _gap = value*10/11; }
        }
    }
}
