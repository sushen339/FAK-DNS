import os
import glob

def convert_conf_to_txt(conf_file, txt_file, cn_dns):
    with open(conf_file, 'r') as conf:
        with open(txt_file, 'w') as txt:
            for line in conf:
                parts = line.strip().split('=')
                if len(parts) != 2:
                    print(f"Invalid line: {line.strip()}")
                    continue
                domain = parts[1].split('/')[1]
                txt.write(f"[/{domain}/]" + cn_dns + "\n")

def main():
    current_directory = os.getcwd()  # 获取当前目录
    converted_directory = os.path.join(current_directory, 'converted')  # 创建 converted 文件夹
    os.makedirs(converted_directory, exist_ok=True)  # 确保 converted 文件夹存在
    
    # 只处理 accelerated-domains.china.conf 文件
    target_file = os.path.join(current_directory, 'accelerated-domains.china.conf')
    
    if not os.path.exists(target_file):
        print(f"文件不存在: {target_file}")
        return
    
    # 生成临时 txt 文件
    temp_txt_file = os.path.join(converted_directory, 'temp.txt')
    convert_conf_to_txt(target_file, temp_txt_file, cn_dns)
    
    # 生成最终的 cn-dns.txt 文件
    final_output = os.path.join(converted_directory, 'cn-dns.txt')
    with open(final_output, 'w') as output_file:
        output_file.write(the_dns + "\n")  # 新增行，内容为自定义内容
        with open(temp_txt_file, 'r') as temp_file:
            output_file.write(temp_file.read())
    
    # 删除临时文件
    os.remove(temp_txt_file)
    print(f"处理完成，输出文件: {final_output}")

# 从环境变量中获取 DNS URL
cn_dns = os.environ.get('CN_DNS')
the_dns = os.environ.get('THE_DNS')

main()
