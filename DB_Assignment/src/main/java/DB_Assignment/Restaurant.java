package DB_Assignment;

public class Restaurant {
    private String name;
    private int starRating;
    private String imagePath;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getStarRating() {
        return starRating;
    }

    public void setStarRating(int starRating) {
        this.starRating = starRating;
    }
        
        
    // 이미지 경로 설정 메서드
    public void setImagePath(String imagePath) {
    	this.imagePath = imagePath;
    }

    // 이미지 경로 가져오는 메서드
    public String getImagePath() {
    	return imagePath;
    }
}
