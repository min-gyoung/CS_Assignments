<%@ page import="java.util.List" %>
<%@ page import="DB_Assignment.Restaurant" %>
<%@ page import="DB_Assignment.DatabaseHandler" %>
<%@ page import="java.sql.Connection, java.sql.DriverManager, java.sql.PreparedStatement, java.sql.ResultSet, java.sql.SQLException" %>
<%@ page import="java.sql.SQLException, java.io.PrintWriter" %>

<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>DB</title>
</head>
<body>    
    <%
        // MariaDB에 연결하기 위한 드라이버 로드
        Class.forName("org.mariadb.jdbc.Driver");
        System.out.println("MariaDB 사용 가능");

        // MariaDB에 연결
        Connection conn = DriverManager.getConnection("jdbc:mariadb://localhost:3306/restaurant","root","0102");
        System.out.println(conn + "<-- conn");

        // SQL 쿼리 준비
        PreparedStatement stmt = conn.prepareStatement("SELECT * FROM restaurant");
        System.out.println(stmt + "<-- stmt");

        // 쿼리 실행 및 결과 가져오기
        ResultSet rs = stmt.executeQuery();
    %>
    <%
        // 가져온 레스토랑 리스트를 받아옴
        List<Restaurant> restaurants = (List<Restaurant>) request.getAttribute("restaurant");
        // 레스토랑 리스트를 다시 request에 담아 index.jsp로 포워딩
        request.setAttribute("restaurant", restaurants);
        request.getRequestDispatcher("index.jsp").forward(request, response);
        
        // 레스토랑 리스트가 비어있지 않을 때 정보를 출력
        if(restaurants != null && !restaurants.isEmpty()) {
            for (Restaurant restaurant : restaurants) {
    %>
                <!-- 레스토랑 정보를 화면에 표시 -->
                <div class="restaurant-square">
                    <h2><%= restaurant.getName() %></h2>
                    <p>별점: <%= restaurant.getStarRating() %></p>
                    <img src="<%= restaurant.getImagePath() %>" alt="레스토랑 이미지">
                </div>
            <%
            }
        } else {
    %>
            <!-- 레스토랑이 없을 경우 메시지 출력 -->
            <p>레스토랑을 찾을 수 없습니다.</p>
        <% } %>
</body>
</html>
