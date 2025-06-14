# API usage guide
This API was developed to provide a native Python integration with all EDL features.

## API setup
Before anything, you should import it and instance the API with:

```python
from edlclient.Library.api import *

e = edl_api()
```

After that, you should set your desired EDL options (those who starts with `--`), e.g. `--debugmode`. For this, you should use the `set_arg()` method, like this:

```python
e.set_arg("--debugmode", True)
```

Be aware that, by default, the `set_arg()` method returns the full arguments dictionary, but, if the passed option doesn't exist, it'll return `Invalid key!`. This should be useful to avoid future errors.

Also, you can use the `reset_arg()` method to set back any option to its default value. This method's return is the same as the `set_arg()`, because it's actually just a wrapper to `set_arg(key, None, True)`.

That said, now you should initialize the API with the `init()` method. However, note that:

1. The API initialization should be done after you set the `--` options

2. To change any `--` option **after** the API initialization, you should reinitialize the API with the `reinit()` method (which is equivalent to `deinit()` + `init()`)

3. You can use the `deinit()` method to "free" the API. This will happen automatically when the API instance (i.e. the Python object) gets destroyed or the program exits

4. Every `init()`/`reinit()`/`deinit()` calls will return the API `status` attribute, which stores a code that can be useful to check if any errors occurred. The stored value will be 1 for error or 0 for success

And, finally, the API is ready to be used!

## EDL commands
In summary, **all EDL commands are API methods** and they follow this same structure: `command([arg1[, arg2[, arg3]]])`. To a better understanding, we're going to take the `peek` command as an example: we know that `peek` requires `<offset>`, `<length>` and `<filename>` as its arguments, respectively. This way, considering the `<offset>` as `0x100000`, `<length>` as `80` and `<filename>` as `output.bin`, we should have this API call:

```python
e.peek(0x100000, 80, "output.bin")
```

And that's it for all the EDL commands! Simple, isn't it?

> For the full command list and their arguments, refer to EDL's documentation (i.e. `edl --help` or `README.md`)

## Basic usage example
This example covers the basic (and probably most common) API usage, so check it out:

```python
from edlclient.Library.api import *

# Step 1
e = edl_api()
e.set_arg("--debugmode", True)
if (e.init() == 1):
	exit(1)

# Step 2
e.peek(0x100000, 80, "peek1.bin")

# Step 3
e.reset_arg("--debugmode")
if (e.reinit() == 1):
	exit(1)

# Step 4
e.peek(0x100080, 80, "peek2.bin")

# Step 5
e.reset()
```

Steps explanation:

1. The API is instanced and initialized with the `--debugmode` option enabled

2. A `peek` command is executed

3. The `--debugmode` option is disabled and, in order to take effect, the API is reinitialized

4. Another `peek` command is executed

5. The Android device is restarted with the `reset` command

For a more contextualized and robust example, check the `Examples/api_example.py`

---
# zh_cn

# API 使用指南
此 API 旨在为所有 EDL 功能提供原生的 Python 集成。

## API 设置
在开始之前，您需要导入 API 并创建其实例：

```python
from edlclient.Library.api import *

e = edl_api()  # 实例化 API 对象
```

之后，您应该设置所需的 EDL 选项（那些以 `--` 开头的），例如 `--debugmode`。为此，您应使用 `set_arg()` 方法，如下所示：

```python
e.set_arg("--debugmode", True)  # 设置 --debugmode 选项为 True
```

请注意，默认情况下，`set_arg()` 方法会返回完整的参数字典。但是，如果传入的选项不存在，它将返回 `Invalid key!`（无效键！）。这有助于避免后续错误。

另外，您可以使用 `reset_arg()` 方法将任何选项重置为其默认值。此方法的返回值与 `set_arg()` 相同，因为它本质上是 `set_arg(key, None, True)` 的包装器。

完成上述设置后，您应该使用 `init()` 方法初始化 API。但是，请注意以下几点：

1.  **API 初始化**应在设置完所有 `--` 选项**之后**进行。
2.  若要在 API 初始化**之后**更改任何 `--` 选项，您应该使用 `reinit()` 方法**重新初始化** API（这等同于 `deinit()` + `init()`）。
3.  您可以使用 `deinit()` 方法来“释放”API。当 API 实例（即 Python 对象）被销毁或程序退出时，此操作会自动发生。
4.  每次调用 `init()` / `reinit()` / `deinit()` 都会返回 API 的 `status` 属性值。该属性存储一个状态码，可用于检查是否发生错误。存储的值将为：1 表示错误，0 表示成功。

最后，API 就绪可以使用了！

## EDL 命令
简而言之，**所有的 EDL 命令都对应 API 方法**，并且它们遵循相同的结构：`command([arg1[, arg2[, arg3]]])`。为了更好地理解，我们以 `peek` 命令为例：我们知道 `peek` 需要 `<offset>`（偏移量）、`<length>`（长度）和 `<filename>`（文件名）作为其参数。因此，假设 `<offset>` 为 `0x100000`，`<length>` 为 `80`，`<filename>` 为 `output.bin`，那么我们应该这样进行 API 调用：

```python
e.peek(0x100000, 80, "output.bin")  # 执行 peek 命令
```

所有 EDL 命令的使用方式都是如此！很简单，不是吗？

> 关于完整的命令列表及其参数，请参考 EDL 的文档（即运行 `edl --help` 或查阅 `README.md`）。

## 基础用法示例
此示例涵盖了基础（也可能是最常见的）API 用法，请参考：

```python
from edlclient.Library.api import *

# 步骤 1: 初始化和设置
e = edl_api()                # 实例化 API 对象
e.set_arg("--debugmode", True) # 启用调试模式
if (e.init() == 1):          # 初始化 API，检查状态
    exit(1)                  # 如果初始化失败 (status=1)，退出程序

# 步骤 2: 执行命令 (带调试模式)
e.peek(0x100000, 80, "peek1.bin") # 执行 peek 命令

# 步骤 3: 更改选项并重新初始化
e.reset_arg("--debugmode")      # 将 --debugmode 重置为默认值 (禁用)
if (e.reinit() == 1):         # 重新初始化 API 使更改生效，检查状态
    exit(1)                  # 如果重新初始化失败，退出程序

# 步骤 4: 执行命令 (不带调试模式)
e.peek(0x100080, 80, "peek2.bin") # 执行另一个 peek 命令

# 步骤 5: 设备操作
e.reset()                     # 使用 reset 命令重启安卓设备
```

步骤解释：

1.  API 被实例化，并在启用 `--debugmode` 选项的情况下初始化。
2.  执行一次 `peek` 命令。
3.  禁用 `--debugmode` 选项，并通过重新初始化 API 使更改生效。
4.  执行另一次 `peek` 命令。
5.  使用 `reset` 命令重启 Android 设备。

如需更详细和健壮的示例，请参考 `Examples/api_example.py` 文件。

---