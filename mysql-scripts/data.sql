USE FabiaNatura;

-- Inserción de datos en la tabla Proveedores
INSERT INTO Proveedores (ruc, nombre) VALUES
('20101796532', 'NATURA COSMETICOS S.A.'),
('20100078792', 'PRODUCTOS AVON S.A.'),
('20517667502', 'ESIKA COSMETICS PERU S.A.C.');

-- Inserción de datos en la tabla Telefonos_Proveedores
INSERT INTO Telefonos_Proveedores (ruc, telefono) VALUES
('20101796532', '440-1362'),
('20100078792', '317-2866'),
('20517667502', '0801-1-3030');

-- Inserción de datos en la tabla Categorias
INSERT INTO Categorias (nombre, descripcion) VALUES
('Maquillaje', 'Productos diseñados para embellecer y resaltar los rasgos del rostro, ofreciendo opciones para diferentes tonos de piel, estilos y ocasiones.'),
('Fragancias', 'Perfumes y colonias para hombres y mujeres, diseñados para reflejar la personalidad y estilo de quien los usa. Estas fragancias suelen estar desarrolladas con notas florales, cítricas, amaderadas o dulces.'),
('Cuidado de la piel', 'Productos especializados para mantener una piel saludable, hidratada y protegida, adaptados a diferentes tipos de piel (seca, grasa, mixta o sensible).'),
('Cuidado del cabello', 'Productos diseñados para limpiar, hidratar, reparar y estilizar el cabello, con opciones para diferentes necesidades capilares.'),
('Bienestar', 'Productos orientados al autocuidado integral, promoviendo la relajación y el equilibrio.');

-- Inserción de Productos de Natura:
INSERT INTO Productos (cod_categoria, ruc, nombre, linea, descripcion, precio_compra, precio_venta, stock, estado) VALUES 
(2, '20101796532', 'Essencial masculino', 'Essencial', 'Amaderado intenso.', 104.5, 125.4, 7, 'disponible'),
(2, '20101796532', 'Kaiak clásico masculino', 'Kaiak', 'Aromático herbal. leve, notas acuosas, albahaca, bergamota.', 64.5, 77.4, 9, 'disponible'),
(2, '20101796532', 'Kriska Shock', 'Kriska', 'Desodorante corporal en spray 100 ml', 93.0, 111.6, 12, 'disponible'),
(2, '20101796532', 'Kaiak urbe masculino', 'Kaiak', 'Aromático herbal. moderado, notas acuosas, sándalo, ámbar.', 64.5, 77.4, 10, 'disponible'),
(2, '20101796532', 'Humor femenino rosa', 'Humor', 'Una fragancia irreverente, enriquecida con ingredientes naturales inéditos brasileños.', 63.0, 75.6, 16, 'disponible'),
(2, '20101796532', 'Ekos frescor pitanga', 'Ekos', 'Notas de pitanga negra conviven con flores de colores y ganan un toque de notas amaderadas.', 61.8, 74.16, 17, 'disponible'),
(2, '20101796532', 'Colonia formas en las nubes', 'Nature', 'Una colonia ideal para acompañar momentos de pura diversión y destapar tu lado creativo.', 64.0, 76.8, 18, 'disponible'),
(2, '20101796532', 'Colonia jugando en los árboles', 'Nature', 'Una invitación a sentir la divertida sensación de jugar en la naturaleza por medio de una fragancia cítrica.', 64.0, 76.8, 15, 'disponible'),
(1, '20101796532', 'Labial cremoso multimix', 'Faces', 'Más capas, más color con efecto cremoso, bye bye a los labios resecos, producto vegano.', 27.0, 32.4, 12, 'disponible'),
(1, '20101796532', 'Esmalte 3D gel negro', 'Una', 'Cobertura uniforme. Favorece la nutrición de las uñas. Larga duración y brillo extraordinario.', 24.0, 28.8, 6, 'disponible'),
(1, '20101796532', 'Esmalte 3D gel marrón', 'Una', 'Cobertura uniforme. Favorece la nutrición de las uñas. Larga duración y brillo extraordinario.', 24.0, 28.8, 4, 'disponible'),
(1, '20101796532', 'Esmalte 3D gel rojo', 'Una', 'Cobertura uniforme. Favorece la nutrición de las uñas. Larga duración y brillo extraordinario.', 24.0, 28.8, 10, 'disponible'),
(1, '20101796532', 'Esmalte 3D gel celeste', 'Una', 'Cobertura uniforme. Favorece la nutrición de las uñas. Larga duración y brillo extraordinario.', 24.0, 28.8, 10, 'disponible'),
(1, '20101796532', 'Maxxi palette de sombras nude', 'Una', 'Alta cobertura. Amplia variedad de tonalidades, desde mate hasta perlado. Para looks naturales hasta los más elaborados.', 102.0, 122.4, 4, 'disponible'),
(3, '20101796532', ' Sérum intensivo multiaclarador', 'Chronos', 'Sérum que ayuda a reducir manchas y unificar el tono de la piel, proporcionando luminosidad y mejorando la textura.', 121.0, 145.2, 3, 'disponible'),
(3, '20101796532', 'Acqua biohidratante', 'Chronos', 'Hidratante ligero que proporciona una hidratación profunda y duradera, ideal para todo tipo de piel.', 141.0, 169.2, 2, 'disponible'),
(3, '20101796532', 'Gel crema antiseñales noche 30 ', 'Chronos', 'Crema nocturna que combate los primeros signos de envejecimiento, mejorando la firmeza y elasticidad de la piel.', 141.0, 169.2, 2, 'disponible'),
(3, '20101796532', 'Protector hidratante antioleosidad FPS 30', 'Chronos', 'Protector solar facial que controla la oleosidad y brinda protección contra los rayos UV, ideal para pieles mixtas a grasas.', 80.0, 96.0, 10, 'disponible'),
(3, '20101796532', 'Pulpa hidratante corporal castaña', 'Chronos', 'Crema corporal que nutre e hidrata profundamente la piel, dejándola suave y perfumada.', 59.0, 70.8, 16, 'disponible'),
(3, '20101796532', 'Crema hidratante corporal frutas rojas', 'Tododia', 'Hidratante corporal de rápida absorción que deja la piel suave y con una fragancia delicada.', 54.3, 65.16, 10, 'disponible'),
(3, '20101796532', 'Hidratante facial aclarador piel seca', 'Faces', 'Hidratante facial que unifica el tono de la piel y proporciona hidratación intensa, especialmente formulado para piel seca.', 33.0, 39.6, 15, 'disponible'),
(3, '20101796532', 'Máscara de arcilla purificante', 'Chronos', 'Mascarilla facial que limpia profundamente, removiendo impurezas y controlando el exceso de oleosidad.', 65.0, 78.0, 7, 'disponible'),
(3, '20101796532', 'Loción protectora facial FPS 50', 'Fotoequilíbrio', 'Protector solar facial para piel normal a seca, que previene el envejecimiento prematuro y es resistente al agua y al sudor hasta por 3 horas.', 80.0, 96.0, 16, 'disponible'),
(3, '20101796532', 'Gel crema protector facial FPS 50', 'Fotoequilíbrio', 'Protector solar facial para piel mixta a oleosa, con textura ligera, rápida absorción y toque seco.', 80.0, 96.0, 5, 'disponible'),
(4, '20101796532', 'Shampoo matizador brillo y protección del color', 'Lumina', 'Realza el brillo y protege el color del cabello teñido, manteniendo su vitalidad por más tiempo.', 34.0, 40.8, 12, 'disponible'),
(4, '20101796532', 'Shampoo estimulante anticaída y crecimiento', 'Lumina', 'Fortalece el cabello y estimula su crecimiento, reduciendo la caída capilar.', 34.0, 40.8, 7, 'disponible'),
(4, '20101796532', 'Shampoo reestructurante limpieza y reparación', 'Lumina', 'Limpia profundamente mientras repara la estructura del cabello dañado, dejándolo más resistente y saludable.', 34.0, 40.8, 13, 'disponible'),
(4, '20101796532', 'Shampoo revitalizante brillo y protección del color', 'Lumina', 'Revitaliza el cabello teñido, aportando brillo y protegiendo el color de los daños diarios.', 34.0, 40.8, 18, 'disponible'),
(4, '20101796532', 'Shampoo nutritivo reparación y nutrición', 'Lumina', 'Proporciona una nutrición profunda, reparando el cabello seco y dejándolo suave y manejable.', 40.0, 48.0, 9, 'disponible'),
(4, '20101796532', 'Crema para peinar modeladora', 'Lumina', 'Define e hidrata el cabello, facilitando el peinado y controlando el frizz.', 34.0, 40.8, 18, 'disponible'),
(4, '20101796532', 'Spray humidificador reactivador de rizos', 'Lumina', 'Reactiva y define los rizos, aportando hidratación y control del frizz durante el día.', 34.0, 40.8, 5, 'disponible'),
(4, '20101796532', 'Óleo leve reparador', 'Lumina', 'Aceite ligero que repara las puntas abiertas y proporciona brillo sin dejar el cabello pesado.', 34.0, 40.8, 8, 'disponible'),
(5, '20101796532', 'Aceite trifásico de maracuyá', 'Ekos', 'Aceite corporal con tres fases que hidratan y perfuman la piel, proporcionando frescura y relajación gracias a las propiedades calmantes del maracuyá.', 62.0, 74.4, 18, 'disponible'),
(5, '20101796532', 'Jabón exfoliante', 'Ekos', 'Jabón en barra con partículas exfoliantes naturales que eliminan células muertas, revitalizan la piel y aportan una fragancia energizante de acaí.', 28.0, 33.6, 17, 'disponible'),
(5, '20101796532', 'Pulpa hidratante para manos de castaña', 'Ekos', 'Crema de manos enriquecida con aceite de castaña, que hidrata y fortalece la piel, dejando las manos suaves y con una agradable fragancia.', 30.0, 36.0, 5, 'disponible'),
(5, '20101796532', 'Aceite de masaje andiroba', 'Ekos', 'Aceite corporal formulado con aceite de andiroba, conocido por sus propiedades antiinflamatorias y relajantes, ideal para masajes que alivian tensiones y promueven el bienestar.', 65.0, 78.0, 6, 'disponible');

-- Inserción de Productos de Avon:

-- Inserción de Productos de Unique: