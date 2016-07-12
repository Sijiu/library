/**
 * Created by Plain on 2016/6/30.
 */
$(function(){
    var a= 0;
    var Test={
        init: function(){
            $(".Title").focus(Test.get_type_head);
        },
        get_type_head: function(){
        }
    };
    $('.typeahead').typeahead({
        source: function (query, process) {
            $.ajax({
                "url": '/test',
                "type": 'POST',
                "dataType": 'JSON',
                "async": true,
                "data": "",
                "success": function (data) {
                    //var arr = [];
                    //for (var i in data) {
                    //    arr.push(data[i]['pdt_name']);
                    //}
                    process(data);
                }
            });
        },
    //    matcher: function (obj) {
    //    var item = JSON.parse(obj);
    //    return ~item.name.toLowerCase().indexOf(this.query.toLowerCase())
    //},
    //
    //sorter: function (items) {
    //    var beginswith = [], caseSensitive = [], caseInsensitive = [], item;
    //    while (aItem = items.shift()) {
    //        var item = JSON.parse(aItem);
    //        if (!item.name.toLowerCase().indexOf(this.query.toLowerCase()))
    //            beginswith.push(JSON.stringify(item));
    //        else if (~item.name.indexOf(this.query)) caseSensitive.push(JSON.stringify(item));
    //        else caseInsensitive.push(JSON.stringify(item));
    //    }
    //
    //    return beginswith.concat(caseSensitive, caseInsensitive)
    //
    //},
    //
    //highlighter: function (obj) {
    //    var item = JSON.parse(obj);
    //    var query = this.query.replace(/[\-\[\]{}()*+?.,\\\^$|#\s]/g, '\\$&')
    //    return item.name.replace(new RegExp('(' + query + ')', 'ig'), function ($1, match) {
    //        return '<strong>' + match + '</strong>'
    //    })
    //},
    //
    //updater: function (obj) {
    //    var item = JSON.parse(obj);
    //    $('#topicId').attr('value', item.id);
    //    return item.name;
    //}

        source:['PHP', 'MySQL', 'SQL', 'PostgreSQL', 'HTML', 'CSS','666', 'HTML5', 'CSS3', 'JSON']
    });
    Test.init();

});
