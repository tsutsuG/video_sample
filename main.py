import cv2
import time
import numpy as np
from my_video import VideoReader

# 動画ファイルのパス
video_path = r"./data/sample_video.mp4"
time_cur = time.perf_counter()
time_old = time_cur


if __name__ == "__main__":
    np.random.seed(int(time.time()))
    
    video_reader = VideoReader()
    video_reader.load(video_path)
    video_reader.resize(0.75)
    
    tms = np.random.randint(20, size=(100,)) - 10
    for i in range(100):
        tms[i] += 250 * i
    
    idx = 0
    
    while True:
        time_cur = time.perf_counter()
        if (time_cur - time_old) > 0.25:
            time_old = time_cur
        else:
            continue

        # ret, frame = video_reader.read()
        ret, frame = video_reader.read_by_ms(tms[idx])
        print(tms[idx], video_reader.cur_frame_no)
        idx += 1

        if not ret:
            print("動画の再生が終了しました。")
            break

        # フレームを表示
        cv2.imshow("Video Frame", frame)
        

        # キー入力待ち
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("動画の再生を中止しました。")
            break
    
    # リソースを開放
    video_reader.release()
    cv2.destroyAllWindows()