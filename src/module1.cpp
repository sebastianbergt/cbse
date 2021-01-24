#include <iostream>

namespace foo {
namespace bar {

class Module1 {
public:
  Module1() {
    std::cout << "test class has been created.\n";
    value_++;
  }

  ~Module1() { std::cout << "test class is being deleted.\n"; }

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
    Module1 m;
    if(m.isValueEven()) {
        std::cout << "value was even\n";
    }
    return 0;
}

} // namespace bar
} // namespace foo