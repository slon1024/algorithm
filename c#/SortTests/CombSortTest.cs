using System.Collections;
using NUnit.Framework;
using Sort;

namespace SortTests
{
    [TestFixture]
    public class CombSortTest : BaseTest
    {
        protected ISort _sort = new CombSort();

        [Test]
        public void testSort()
        {
            var expected = (ArrayList)_values.Clone();
            expected.Sort();

            var actual = _sort.Sort(_values);

            Assert.That(expected, Is.EqualTo(actual));
        }

    }
}