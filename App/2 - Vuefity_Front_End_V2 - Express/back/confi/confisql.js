module.exports = { // variavel para exportar esse modulo. 
    dialect: 'mysql',
    host: 'localhost',
    username: 'root',
    password: '0101',
    database: 'exemplo',
    define:{
        timestamps: true, // createdat e updatedet. Indica quando foi criado a atualizado. 
        underscored: true, // ira colocar todas as os espaços com _ (Formato snaked case)
    },
};


// module export=
// (property) export=:{
//     dialect: string;
//     host: string;
//     username: string;
//     password: string;
//     database: string;
//     define: {
//         timestamps: boolean;
//         underscored: boolean;
//     };
// }

