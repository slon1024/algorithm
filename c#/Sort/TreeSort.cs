using System.Collections;


namespace Sort
{
    public class Tree
    {
        private Tree _left;
        private Tree _right;
        private int _key;

        public Tree Left
        {
            get { return _left; }
            set
            {
                if(null == _left)
                    _left = value;
                else
                    _left.Insert(value);
                
            }
        }

        public Tree Right
        {
            get { return _right; }
            set
            {
                if (null == _right)
                    _right = value;
                else
                    _right.Insert(value);
            }
        }



        public Tree(int key)
        {
            _key = key;
        }

        public void Insert(Tree tree)
        {
            if(tree._key < _key)
                Left = tree;
            else
                Right = tree;
        }

        public ArrayList ToArrayList()
        {
            var result = new ArrayList();
            if (null != Left)
                result.AddRange( Left.ToArrayList() );
            result.Add(_key);
            if (null != Right)
                result.AddRange(Right.ToArrayList());

            return result;
        }
       
    }

    public class TreeSort : ISort
    {
        public ArrayList Sort(ArrayList inArray)
        {
            if (inArray.Count < 1)
                return inArray;

            var tree = new Tree((int)inArray[0]);
            for (int i = 1; i < inArray.Count; i++ )
                tree.Insert(new Tree((int)inArray[i]));

            return tree.ToArrayList();
        }
    }
}
