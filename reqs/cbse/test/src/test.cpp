#include <iostream>

namespace foo {
namespace bar {

class TestClass {
public:
  TestClass() {
    std::cout << "test class has been created.\n";
    value_++;
  }

  ~TestClass() { std::cout << "test class is being deleted.\n"; }

  bool isValueEven() {
    if (value_ % 2 == 0) {
      return true;
    } else {
      return false;
    }
  }

private:
  int value_{0};
};

int main(int argc, char* argv[]) {
    TestClass t;
    if(t.isValueEven()) {
        std::cout << "value was even\n";
    }
    return 0;
}

} // namespace bar
} // namespace foo