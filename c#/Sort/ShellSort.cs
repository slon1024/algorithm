using System.Collections;

namespace Sort
{
    public class ShellSort : ISort
    {
        public ArrayList Sort(ArrayList inArray)
        {
            Gap = inArray.Count;
            while (Gap > 1)
            {
                Gap = Gap;
                int i = Gap;

                while(i < inArray.Count)
                {
                    int current = (int)inArray[i], j = i - Gap;
                    while(j>-1 && (int)inArray[j] > current)
                    {
                        inArray[j + Gap] = inArray[j];
                        j -= Gap;
                    }
                    inArray[j + Gap] = current;
                    i += Gap;
                }
            }
            return inArray;
        }

        private int _gap;
        public int Gap
        {
            get { return _gap; }
            set { _gap = value * 10 / 11; }
        }
    }
}
