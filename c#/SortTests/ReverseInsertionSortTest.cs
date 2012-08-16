using System.Collections;
using NUnit.Framework;
using Sort;

namespace SortTests
{
    [TestFixture]
    public class ReverseInsertionSortTest : BaseTest
    {
        protected ISort _sort = new ReverseInsertionSort();

        [Test]
        public void testSort()
        {
            var expected = (ArrayList)_values.Clone();
            expected.Sort();
            expected.Reverse();

            var actual = _sort.Sort(_values);

            Assert.That(expected, Is.EqualTo(actual));
        }

    }
}