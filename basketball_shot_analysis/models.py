class Shot:
    def __init__(self, id: int, accuracy: float, angle: float, trajectory: float):
        self.id = id
        self.accuracy = accuracy
        self.angle = angle
        self.trajectory = trajectory

    def get_accuracy(self) -> float:
        return self.accuracy

    def get_angle(self) -> float:
        return self.angle

    def get_trajectory(self) -> float:
        return self.trajectory


class Video:
    def __init__(self, id: int, file_path: str):
        self.id = id
        self.file_path = file_path
        self.shots = []

    def get_shots(self) -> List[Shot]:
        return self.shots

    def add_shot(self, shot: Shot) -> None:
        self.shots.append(shot)


class ShotAnalyzer:
    def analyze_video(self, video: Video) -> List[Shot]:
        analyzed_shots = []
        for shot in video.get_shots():
            analyzed_shot = self.analyze_shot(shot)
            analyzed_shots.append(analyzed_shot)
        return analyzed_shots

    def analyze_shot(self, shot: Shot) -> Shot:
        # Perform shot analysis here
        return shot


class Database:
    def save_video(self, video: Video) -> None:
        # Save video to database
        pass

    def get_video(self, id: int) -> Video:
        # Retrieve video from database
        pass

    def get_all_videos(self) -> List[Video]:
        # Retrieve all videos from database
        pass


class API:
    def upload_video(self, file_path: str) -> int:
        # Upload video and return video ID
        pass

    def analyze_video(self, video_id: int) -> List[Shot]:
        # Analyze video and return analyzed shots
        pass


class WebApp:
    def show_video(self, video_id: int) -> None:
        # Display video on web app
        pass

    def show_analysis(self, video_id: int) -> None:
        # Display analysis of video on web app
        pass


class Chart:
    def show_accuracy_chart(self, shots: List[Shot]) -> None:
        # Display accuracy chart based on shots
        pass

    def show_angle_chart(self, shots: List[Shot]) -> None:
        # Display angle chart based on shots
        pass

    def show_trajectory_chart(self, shots: List[Shot]) -> None:
        # Display trajectory chart based on shots
        pass


class User:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def upload_video(self, file_path: str) -> None:
        # Upload video based on user role
        pass

    def analyze_video(self, video_id: int) -> List[Shot]:
        # Analyze video based on user role
        pass


class Coach(User):
    def show_analysis(self, video_id: int) -> None:
        # Show analysis of video for coach
        pass


class Player(User):
    def upload_video(self, file_path: str) -> None:
        # Upload video for player
        pass


class Analyst(User):
    def show_analysis(self, video_id: int) -> None:
        # Show analysis of video for analyst
        pass


class Fan(User):
    def show_analysis(self, video_id: int) -> None:
        # Show analysis of video for fan
        pass


class Developer(User):
    def upload_video(self, file_path: str) -> None:
        # Upload video for developer
        pass

    def analyze_video(self, video_id: int) -> List[Shot]:
        # Analyze video for developer
        pass
