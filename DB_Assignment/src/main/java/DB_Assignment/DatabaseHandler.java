package DB_Assignment;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.ResultSet;
import java.sql.Statement;

public class DatabaseHandler {

    public static void main(String[] args) {
        // 데이터베이스 연결을 위한 변수 초기화
        Connection conn = null; // 데이터베이스 연결을 위한 Connection 객체
        Statement stmt = null; // SQL 문을 실행하기 위한 Statement 객체
        ResultSet result = null; // 쿼리 실행 결과를 저장하기 위한 ResultSet 객체
        
        try {
            // JDBC 드라이버 로드
            Class.forName("org.mariadb.jdbc.Driver");

            // 데이터베이스 연결을 위한 정보 설정
            String jdbcDriver = "jdbc:mariadb://localhost:3306/restaurant"; // 데이터베이스 URL
            String dbUser = "root"; // 데이터베이스 사용자 이름
            String dbPass = "0102"; // 데이터베이스 비밀번호
            String query = "SHOW TABLES;"; // 실행할 SQL 쿼리

            // 데이터베이스에 연결
            conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPass);

            // Statement 객체 생성
            stmt = conn.createStatement();

            // 검색어에 기반하여 준비된 SQL 쿼리 실행
            String query1 = "SELECT * FROM restaurant"; // restaurant 테이블에서 모든 열 선택하는 SQL 쿼리

            // 쿼리 실행
            result = stmt.executeQuery(query); // SHOW TABLES; 쿼리 실행

            // 결과를 반복적으로 가져와서 출력
            while (result.next()) {
                System.out.println(result.getString(1)); // 결과의 첫 번째 열 값을 출력
            }
        } catch (Exception e) {
            e.printStackTrace(); // 예외 발생 시 에러 내용 출력
        } finally {
            try {
                // 연결, Statement, ResultSet 닫기 (자원 해제)
                if (conn != null) conn.close();
                if (stmt != null) stmt.close();
                if (result != null) result.close();
            } catch (SQLException e) {
                e.printStackTrace(); // SQLException 발생 시 에러 내용 출력
            }
        }
    }
}