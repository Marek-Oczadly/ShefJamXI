#include <string>
#include <filesystem>
#include <algorithm>
#define fs std::filesystem

class FileManager {
private:

    struct FileArr {
        std::string* const file_list;
        const unsigned int num_files;
        const std::string directory;
    };
    const FileArr file_list;

    static FileArr listDir(const std::string& directory) {
        unsigned short file_count = 0;
        for (const auto& i : fs::directory_iterator(directory)) {
            ++file_count;
        }
        std::string* files = new std::string[file_count];
        std::string* f_ptr = files;
        for (const auto &i : fs::directory_iterator(directory)) {
            if (i.is_regular_file()) {
                *f_ptr = i.path().filename().string();
            }
        }
        std::sort(files, files+file_count);
        return FileArr({files, file_count, directory});
    }

    const std::string* find(const std::string& val) const {
        const std::string* l = file_list.file_list;
        const std::string* r = file_list.file_list + file_list.num_files;
        while (r > l) {
            auto mid = l + (r - l) / 2;
            if (*mid == val) return mid;
            else if (*mid > val) l = mid + 1;
            else r = mid - 1;
        }
        return nullptr;
    }
public:
    FileManager(const std::string& directory) :
        file_list(listDir(directory)) {}
    
    bool isFile(const std::string& val) const noexcept {
        return (find(val) != nullptr);
    }

    bool isFileName(const std::string& val) const noexcept {
        if (!isFile(val + ".png")) return isFile(val + ".jpg");
        return true;
    }
};