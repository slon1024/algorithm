using System.Collections;

namespace Sort
{
    public class GnomeSort : ISort
    {
        public ArrayList Sort(ArrayList inArray)
        {
            int current = 0;
            int next = current + 1;

            while (next < inArray.Count)
            {
                if( (int)inArray[current] > (int)inArray[next] )
                {
                    var tmp = inArray[current];
                    inArray[current] = inArray[next];
                    inArray[next] = tmp;

                    if (current > 0)
                        current--;
                }
                else
                {
                    current++;
                }

                next = current + 1;
            }

            return inArray;
        }
    }
}
