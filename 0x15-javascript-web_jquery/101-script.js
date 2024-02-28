 $(document).ready(function() {
            
            $("body").on("click", "DIV#add_item", function() {
                
                const newItem = $("<li>Item</li>");
                
                $("UL.my_list").append(newItem);
            });
            
            $("body").on("click", "DIV#remove_item", function() {
                
                $("UL.my_list li:last-child").remove();
            });
            
            $("body").on("click", "DIV#clear_list", function() {
                $("UL.my_list").empty();
            });
        });
