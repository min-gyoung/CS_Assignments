//package DB_Assignment;
//
//import java.io.IOException;
//import java.util.List;
//
//import jakarta.servlet.RequestDispatcher;
//import jakarta.servlet.ServletException;
//import jakarta.servlet.annotation.WebServlet;
//import jakarta.servlet.http.HttpServlet;
//import jakarta.servlet.http.HttpServletRequest;
//import jakarta.servlet.http.HttpServletResponse;
//
//@WebServlet("/loadRestaurants")
//public class RestaurantServlet extends HttpServlet {
//    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
//        DatabaseHandler dbHandler = new DatabaseHandler();
//        List<Restaurant> restaurants = dbHandler.getAllRestaurants();
//
//        request.setAttribute("restaurants", restaurants);
//        RequestDispatcher dispatcher = request.getRequestDispatcher("displayRestaurants.jsp");
//        dispatcher.forward(request, response);
//    }
//}