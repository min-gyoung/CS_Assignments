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
    <title>Restaurant DB</title>
    <style>
        .restaurant-square {
            border: 1px solid #ccc;
            padding: 10px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

<h1 style="text-align: center;">Restaurant DB</h1>
<h3 style="text-align: center;">Majiri Restaurant Information Recommendation Database</h3><br><br>

<form action="displayRestaurants.jsp" method="GET" style="text-align: center;">
    <input type="text" name="searchQuery" placeholder="Search for a restaurant" size="40" style="height: 30px;">
    <input type="submit" value="Search" style="height: 35px; width: 100px;">
</form>

<div id="restaurantList">
    <%
        try {
            // MariaDB 데이터베이스에 연결을 설정합니다.
            Class.forName("org.mariadb.jdbc.Driver");
            Connection conn = DriverManager.getConnection("jdbc:mariadb://localhost:3306/your_database", "username", "password");

            String searchQuery = request.getParameter("searchQuery");
            String sqlQuery;

            // 만약 검색 쿼리가 제공되었고 비어있지 않다면, 입력된 검색어를 포함하는 레스토랑 정보를 검색
            if (searchQuery != null && !searchQuery.isEmpty()) {
                sqlQuery = "SELECT * FROM restaurant WHERE name LIKE ?";
                PreparedStatement stmt = conn.prepareStatement(sqlQuery);
                stmt.setString(1, "%" + searchQuery + "%");
                ResultSet rs = stmt.executeQuery();

                // 검색 결과를 기반으로 레스토랑 정보를 화면에 출력
                while (rs.next()) {
    %>
                    <div class="restaurant-square">
                        <h3><%= rs.getString("name") %></h3>
                        <p>Star Rating: <%= rs.getInt("star_rating") %></p>
                    </div>
    <%
                }
                rs.close();
                stmt.close();
            } else {
                // 검색어가 제공되지 않았을 때, 모든 레스토랑 정보를 가져와 출력
                PreparedStatement stmt = conn.prepareStatement("SELECT * FROM restaurant");
                ResultSet rs = stmt.executeQuery();

                // 모든 레스토랑 정보를 화면에 출력
                while (rs.next()) {
    %>
                    <div class="restaurant-square">
                        <h3><%= rs.getString("name") %></h3>
                        <p>Star Rating: <%= rs.getInt("star_rating") %></p>
                        <!-- 각 레스토랑의 이미지를 출력 -->
                        <img src="<%= rs.getString("./src/images") %>" alt="Restaurant Image">
                    </div>
    <%
                }
                rs.close();
                stmt.close();
            }
            conn.close();
        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    %>
</div>
</body>
</html>