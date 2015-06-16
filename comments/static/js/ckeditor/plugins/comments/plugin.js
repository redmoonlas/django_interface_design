/**
 * Copyright (c) 2014, CKSource - Frederico Knabben. All rights reserved.
 * Licensed under the terms of the MIT License (see LICENSE.md).
 *
 * Basic sample plugin inserting current date and time into the CKEditor editing area.
 *
 * Created out of the CKEditor Plugin SDK:
 * http://docs.ckeditor.com/#!/guide/plugin_sdk_intro
 */

// Register the plugin within the editor.
CKEDITOR.plugins.add( 'comments', {

	// Register the icons. They must match command names.
	icons: 'comment',
	hidpi: true,
	// The plugin initialization logic goes inside this method.
	init: function( editor ) {

		// Define the editor command that inserts a timestamp.
		editor.addCommand( 'insertComment', {

			// Define the function that will be fired when the command is executed.
			exec: function( editor ) {
				// Insert the timestamp into the document.
				//editor.insertHtml( '<div comment=\'true\'>New Comment</div>' );
				var selected_text = editor.getSelection().getSelectedText();
				if (selected_text)
				{
					var newElement = editor.document.createElement( 'span' );
					var get_id = editor.config.comment_get_id;
					var id = get_id();
					newElement.setAttributes({
						'data-cid': id,
						class: 'comment',
						style: 'background-color:yellow;cursor:pointer;'
					}) ;
					newElement.setText(selected_text);
					editor.insertElement(newElement);
				}

			}
		});

		// Create the toolbar button that executes the above command.
		editor.ui.addButton( 'Comment', {
			label: 'Insert Comment',
			command: 'insertComment',
			toolbar: 'comments'
		});

		editor.on('contentDom', function() {
			var editable = editor.editable();
			editable.attachListener( editable, 'click', function(evt) {
				var element = evt.data.getTarget();
				if (element.hasClass('comment'))
				{
					console.log(element);
					var callback = editor.config.comment_onclick;
					callback();
				}

			});
		});
	}
});

CKEDITOR.config.comment_get_id = function() {
	return 1;
}

CKEDITOR.config.comment_onclick = function() {
	return;
}
