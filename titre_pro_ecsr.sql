-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 25, 2025 at 10:36 AM
-- Server version: 8.4.3
-- PHP Version: 8.3.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `titre_pro_ecsr`
--

-- --------------------------------------------------------

--
-- Table structure for table `eleves_eleve`
--

CREATE TABLE `eleves_eleve` (
  `id` bigint NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `date_naissance` date DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `date_inscription` date NOT NULL,
  `neph` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `eleves_eleve`
--

INSERT INTO `eleves_eleve` (`id`, `prenom`, `nom`, `date_naissance`, `email`, `telephone`, `date_inscription`, `neph`) VALUES
(1, 'Frodo', 'Baggins', '2008-08-18', 'frodobaggins@culdesac.com', '0700000000', '2025-08-29', '25081220'),
(2, 'Tiffany', 'Faa', NULL, 'faatiffany@gmail.com', NULL, '2025-08-29', NULL),
(3, 'Sirine', 'Fille de Nawel', NULL, NULL, NULL, '2025-09-04', NULL),
(4, 'Ikhvan', 'Bitsiev', NULL, NULL, '06 49 24 23 13', '2025-09-05', NULL),
(5, 'Yanis', 'Hurad Albinet', '2005-05-31', NULL, NULL, '2025-10-02', '230912200052'),
(6, 'Julian', 'Moity', '2006-12-11', NULL, NULL, '2025-10-06', '21018110290'),
(7, 'samrane', 'Amadi', NULL, NULL, NULL, '2025-10-07', '241212200192'),
(8, 'Jordan', 'Leonie', '2006-03-20', NULL, NULL, '2025-10-14', '240612200290');

-- --------------------------------------------------------

--
-- Table structure for table `eleves_progression`
--

CREATE TABLE `eleves_progression` (
  `id` bigint NOT NULL,
  `date_cours` date NOT NULL,
  `commentaire` longtext NOT NULL,
  `valide` tinyint(1) NOT NULL,
  `eleve_id` bigint NOT NULL,
  `heure_cours` time(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `eleves_progression`
--

INSERT INTO `eleves_progression` (`id`, `date_cours`, `commentaire`, `valide`, `eleve_id`, `heure_cours`) VALUES
(2, '2025-08-29', 'test de commentaires', 0, 1, '12:09:45.000000'),
(3, '2025-08-29', 'test d\'ajout de commentaire via le bouton', 0, 1, '11:30:00.000000'),
(4, '2025-08-29', '<h1><span style=\"color:#2ecc71\">Test de la mise en forme du texte</span></h1>\r\n\r\n<hr />\r\n<h2 style=\"font-style:italic\"><u>Ca fonctionne&nbsp;<img alt=\"laugh\" src=\"http://127.0.0.1:8000/static/ckeditor/ckeditor/plugins/smiley/images/teeth_smile.png\" style=\"height:23px; width:23px\" title=\"laugh\" /></u></h2>\r\n\r\n<p>&nbsp;</p>', 0, 1, '15:54:00.000000'),
(6, '2025-09-11', '', 0, 3, '09:00:00.000000'),
(7, '2025-09-05', '', 0, 3, '10:31:00.000000'),
(8, '2025-09-10', '<p>Vu demarage , point de patinage, chaine cin&egrave;matique,</p>', 0, 2, '08:40:00.000000'),
(9, '2025-09-17', '<p>Suite sur d&eacute;marrage, contenue th&eacute;orique compris, contenue pratique &agrave; travailler encore, se crispe d&egrave;s qu&#39;elle fait une erreur.</p>', 0, 2, '10:23:00.000000'),
(10, '2025-09-10', '<p>Travail du demarage en cote, appr&eacute;hende le recul de la voiture. Maintient du pdp presque assimiler, a travailler encore , d&eacute;marrage a plat correct a voir la gestion du volant ( circu )&nbsp;</p>', 0, 2, '13:24:00.000000'),
(11, '2025-09-10', '<p>Savoir d&eacute;marer sans cal&eacute; sans a coup, savoir s&#39;arr&ecirc;ter sans cal&eacute;&nbsp;</p>\r\n\r\n<p>Trop de pr&eacute;cipitations sur le point de patinage,&nbsp; th&eacute;orie ok&nbsp;</p>\r\n\r\n<p>Quelque demarage parfait, arr&ecirc;t plus que ok&nbsp;</p>', 0, 2, '15:15:00.000000'),
(12, '2025-09-11', '<p>Cour, sur tourner le volant et redresser, sentiment de regression. Donc ne pas rester l&agrave; dessu. Pcour: A voir si volant avec les p&eacute;dales en plus moins de difficult&eacute;s .</p>', 0, 2, '09:01:00.000000'),
(13, '2025-09-11', '<p>Travail du point de patinage. Technique des 3secondes pour plus de souplesse.</p>\r\n\r\n<p>En progr&egrave;s. Assimil&eacute;&nbsp;</p>\r\n\r\n<p>Travail sur sensibilit&eacute; des p&eacute;dales.</p>\r\n\r\n<p>Surveiller volant.</p>', 0, 2, '10:30:00.000000'),
(14, '2025-09-11', '<p>Travail angle mort 💀 explication et utilit&eacute;, travail en circu et d&eacute;tection des angles mort.&nbsp;</p>\r\n\r\n<p>Continuer sur ca et insister sur la proc&eacute;dure a chaque fois qu&#39;elle bouge le v&eacute;hicules&nbsp;</p>\r\n\r\n<p>Attention encore placement sur la chausse&nbsp;</p>', 0, 2, '13:10:00.000000'),
(15, '2025-09-11', '<p>Travaill&eacute; sur le dosage du frein, net progr&egrave;s, enchainer sur l&#39;arr&ecirc;t de pr&eacute;cision puis sur une autre comp&eacute;tence&nbsp;</p>', 0, 2, '15:15:00.000000'),
(16, '2025-09-17', '<p>D&eacute;marrage en c&ocirc;te avec frein a main&nbsp;</p>\r\n\r\n<p>Arr&ecirc;t de pr&eacute;cision&nbsp;</p>\r\n\r\n<p>&nbsp;</p>', 0, 2, '08:48:00.000000'),
(17, '2025-09-16', '<p>Vu freinage de pr&eacute;cision a continuer</p>\r\n\r\n<p>Attention se mets la pression quand y a de la circu</p>\r\n\r\n<p>A revoir demarrage cote</p>', 0, 2, '10:40:00.000000'),
(18, '2025-09-17', '<p>Travail d&eacute;marrage en cote et arr&ecirc;t de precision</p>\r\n\r\n<p>Net progr&egrave;s, arr&ecirc;t de pr&eacute;cision &agrave; peaufiner</p>\r\n\r\n<p>Demarrage en c&ocirc;te ok</p>', 0, 2, '13:27:00.000000'),
(19, '2025-09-17', '<p>Vue passage vitesse jusqu&#39;&agrave; la 4, abord&eacute; sans faire la 5 et 6. Avec accompagnement verbal ok , s automiser sur l action. Attention pas vu retrogradage.&nbsp;</p>', 0, 2, '15:05:00.000000'),
(20, '2025-09-18', '<p>Monter et descente de vitesse a travailler&nbsp;</p>\r\n\r\n<p>Contr&ocirc;le environnement angle mort a automatis&eacute;&nbsp;</p>\r\n\r\n<p>Toujours le giga stress de la circu&nbsp;</p>\r\n\r\n<p>&nbsp;</p>', 0, 2, '08:38:00.000000'),
(21, '2025-09-18', '<p>Vue passage vitesse et retrogradage. Ne pas rajouter les contr&ocirc;les pr le moment,&nbsp;</p>\r\n\r\n<p>Attention ⚠ tourne &agrave; gauche ! Pas couper la ligne.&nbsp;</p>\r\n\r\n<p>Decomposer &ecirc;tre accompagn&eacute; de paroles, oublier les gens autour. Vieiller &agrave; anticiper plus l accompagnement au retrogradage pour qu elle ai le temps de le faire .</p>', 0, 2, '10:37:00.000000'),
(22, '2025-09-18', '<p>Vu passage et retrogradage&nbsp;</p>\r\n\r\n<p>Revoir passage de vitesse h&eacute;sitation tromp&eacute;</p>\r\n\r\n<p>Revoir balance de pied</p>', 0, 2, '13:20:00.000000'),
(23, '2025-10-02', '<p>Savoir adapt&eacute; son allure aux intersections et sycroniser les contr&ocirc;le.</p>', 0, 5, '08:40:00.000000'),
(24, '2025-10-02', '<p>Bien dans l&#39;ensemble, souvent trop a gauche lors de la sortie des intersections.&nbsp;</p>\r\n\r\n<p>Mieux anticip&eacute; les intersection ( savoir si j&#39;ai le temps)</p>\r\n\r\n<p>Attention au stop</p>\r\n\r\n<p>&nbsp;</p>', 0, 5, '10:30:00.000000'),
(25, '2025-10-02', '<p>Travail de l,angle mort ; a automatis&eacute; un maximum revoir les rond point&nbsp;</p>', 0, 5, '13:10:00.000000'),
(26, '2025-10-02', '<p>Petit exc&egrave;s de dynamisme. Allure pas tjs adapt&eacute;. Attention aux contr&ocirc;les .</p>', 0, 5, '14:55:00.000000'),
(27, '2025-09-18', '<p><u>Savoir s&#39;organiser m&eacute;caniquement &agrave; l&#39;approche d&#39;une intersection.</u></p>\r\n\r\n<p>- vu les diff&eacute;rentes phases de l&#39;approche d&#39;une intersection: contr&ocirc;les, cligno, placement, adaptation allure</p>\r\n\r\n<p>bonne progression, moins de stress et plus de disponibilit&eacute;</p>', 0, 2, '15:20:00.000000'),
(28, '2025-10-03', '<p>Travail sur contr&ocirc;les en agglom&eacute;ration, se rend compte des erreurs qu&#39;il peut faire, tr&egrave;s bonne progression</p>', 0, 5, '08:51:00.000000'),
(29, '2025-10-03', '<p>Vu se garer, epis avant, en s&eacute;curit&eacute;, contr&ocirc;le, cligno et allure lente. Attention ⚠ signaler son intention de !</p>\r\n\r\n<p>Vu se garer comme il faut dans l emplacement .</p>', 0, 5, '10:30:00.000000'),
(30, '2025-10-03', '<p>Vu retour premi&egrave;re&nbsp;</p>\r\n\r\n<p>A voir placement giratoire</p>\r\n\r\n<p>A voir la prise de d&eacute;cision&nbsp;</p>', 0, 5, '13:05:00.000000'),
(31, '2025-10-03', '<p>Des erreurs sur les placement pour tourner &agrave; gauche et &agrave;&nbsp; droite</p>\r\n\r\n<p>Savoir se placer pour tourner dans les intersection .</p>\r\n\r\n<p>En progr&egrave;s, a renforcer&nbsp;</p>', 0, 5, '15:08:00.000000'),
(32, '2025-09-29', '<p>Vu epi av et ar</p>\r\n\r\n<p>Regaerder le controle</p>', 0, 6, '13:15:00.000000'),
(33, '2025-10-07', '<p>Premi&egrave;re le&ccedil;on. Installation au poste de conduite. Tour du vh, v&eacute;rif ext&eacute;rieure. Abord&eacute; volant.</p>', 0, 7, '08:45:00.000000'),
(34, '2025-10-07', '<p>Vu le volant sur piste. Tourne &agrave; gauche, tourner a droite . Rep&egrave;res pour bien tourner en angle droit et rester sur sa trajectoire .&nbsp;</p>', 0, 7, '10:21:00.000000'),
(35, '2025-10-07', '<p>Vue manip volant, point de pivot travail tourner gauche et droite en circulation plutoto a l&#39;aise&nbsp;</p>', 0, 7, '13:05:00.000000'),
(37, '2025-10-10', '<p>D&eacute;marrage en cote avec et sans frein a main</p>\r\n\r\n<p>Revoir les d&eacute;marrage et les placements&nbsp;</p>\r\n\r\n<p>&nbsp;</p>', 0, 5, '08:45:00.000000'),
(38, '2025-10-10', '<p>D&eacute;marrage en c&ocirc;te au frein &agrave; main r&eacute;ussi. Travail placement giratoire &agrave; renforcer, attention &agrave; l&#39;allure.</p>', 0, 5, '10:30:00.000000'),
(39, '2025-10-10', '<p>Re travail des contr&ocirc;les et angle mort 💀 progression sur l&#39;automatisme attention signale avant les contr&ocirc;les&nbsp;</p>\r\n\r\n<p>A travailler&nbsp;</p>', 0, 5, '13:25:00.000000'),
(40, '2025-10-10', '<p>Vue insertion dynamique mais attention allure, et regard avant insertion. Dynamique veut pas dire vite.</p>', 0, 5, '15:15:00.000000'),
(41, '2025-10-14', '<p>Vu contr&ocirc;le angle morts et organisation avant intersection</p>', 0, 8, '08:54:00.000000'),
(42, '2025-10-14', '<p>Savoir faire un demie tour en toute securit&eacute;.</p>\r\n\r\n<p>Marche arri&egrave;re ligne droite ( non r&eacute;aliser )</p>', 0, 8, '10:15:00.000000'),
(43, '2025-10-14', '<p>Demi-tour valid&eacute;, marche arri&egrave;re droite aussi. Attention debraie un peu t&ocirc;t .</p>', 0, 8, '13:16:00.000000'),
(44, '2025-10-14', '<p>Travail de l&#39;angle mort, en circu et parking, a automatiser, belle compr&eacute;hension du point&nbsp;</p>', 0, 8, '14:53:00.000000'),
(45, '2025-10-15', '<p>Reprendre l habitude du dosage acc&eacute;l&eacute;rateur et frein et de passer les vitesses. Reprendre confiance.</p>\r\n\r\n<p>Point de travail r&eacute;alis&eacute;: reprendre en main la voiture et les proc&eacute;dures .</p>', 0, 2, '08:52:00.000000'),
(46, '2025-10-15', '<p>Travail sur bo&icirc;te de vitesse et le d&eacute;marrage en c&ocirc;te</p>\r\n\r\n<p>&Agrave; continuer</p>', 0, 2, '10:28:00.000000'),
(47, '2025-10-15', '<p>Ce met trop la pression quand il y a du monde&nbsp;</p>\r\n\r\n<p>Renforcement g&eacute;n&eacute;ral&nbsp;</p>\r\n\r\n<p>Abord&eacute; la th&eacute;orie marche ar</p>', 0, 2, '14:47:00.000000'),
(48, '2025-10-24', '<p>Vue d&eacute;composition des geste pour conduire pour &ecirc;tre sereine sur la route. Prendre le temps de faire choses.</p>', 0, 2, '09:15:00.000000'),
(49, '2025-10-31', '', 0, 2, '10:45:00.000000'),
(50, '2025-10-25', '<p>Revu le passage et retrogadage de vitesse.</p>\r\n\r\n<p>Attention a la synchronisation&nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>', 0, 2, '10:45:00.000000'),
(51, '2025-10-24', '<p>Gestion globale de l&#39;allure du v&eacute;hicule (ralentir, acc&eacute;l&eacute;rer, freiner, tourner, rn conditions de circulations )</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Bon progr&egrave;s globalement, attention a se donner le temps d&#39;analyser</p>', 0, 2, '13:15:00.000000');

-- --------------------------------------------------------

--
-- Table structure for table `themes_categorie`
--

CREATE TABLE `themes_categorie` (
  `id` bigint NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `themes_categorie`
--

INSERT INTO `themes_categorie` (`id`, `name`) VALUES
(12, 'Alcool'),
(11, 'Biomécanique'),
(4, 'Circulation'),
(17, 'Environnement'),
(7, 'Homme'),
(18, 'Législation'),
(10, 'Partage social'),
(3, 'Permis'),
(13, 'Physiologie'),
(8, 'Psychoactif'),
(5, 'Reglementation'),
(14, 'Risques'),
(16, 'Sanction'),
(6, 'Signalisation'),
(15, 'Statistiques'),
(2, 'Technologie'),
(1, 'Véhicule'),
(9, 'Vitesse');

-- --------------------------------------------------------

--
-- Table structure for table `themes_contentblock`
--

CREATE TABLE `themes_contentblock` (
  `id` bigint NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `texte` longtext,
  `image` varchar(100) DEFAULT NULL,
  `ordre` int UNSIGNED NOT NULL,
  `theme_id` bigint NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `themes_reglementation`
--

CREATE TABLE `themes_reglementation` (
  `id` bigint NOT NULL,
  `lettre` varchar(1) NOT NULL,
  `numero_article` varchar(10) NOT NULL,
  `date_version` date NOT NULL,
  `contenu` longtext NOT NULL,
  `amende` longtext,
  `retrait_points` int UNSIGNED NOT NULL,
  `theme_id` bigint DEFAULT NULL
) ;

--
-- Dumping data for table `themes_reglementation`
--

INSERT INTO `themes_reglementation` (`id`, `lettre`, `numero_article`, `date_version`, `contenu`, `amende`, `retrait_points`, `theme_id`) VALUES
(1, 'L', '234-1', '2025-07-09', 'Même en l\'absence de tout signe d\'ivresse manifeste, le fait de conduire un véhicule sous l\'empire d\'un état alcoolique caractérisé par une concentration d\'alcool dans le sang égale ou supérieure à 0,80 gramme par litre ou par une concentration d\'alcool dans l\'air expiré égale ou supérieure à 0,40 milligramme par litre.\r\nLes dispositions du présent article sont applicables à l\'accompagnateur d\'un élève conducteur.', '9000 €', 6, 5),
(2, 'L', '234-8', '2019-12-24', 'Le fait de refuser de se soumettre aux vérifications prévues par les articles L. 234-4 à L. 234-6 ou aux vérifications prévues par l\'article L. 234-9', '4500 €', 6, 5);

-- --------------------------------------------------------

--
-- Table structure for table `themes_reglementation_sanctions`
--

CREATE TABLE `themes_reglementation_sanctions` (
  `id` bigint NOT NULL,
  `reglementation_id` bigint NOT NULL,
  `sanction_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `themes_reglementation_sanctions`
--

INSERT INTO `themes_reglementation_sanctions` (`id`, `reglementation_id`, `sanction_id`) VALUES
(1, 1, 1),
(2, 1, 3),
(3, 1, 4),
(4, 1, 5),
(5, 1, 6),
(6, 1, 7),
(7, 1, 8),
(8, 1, 9),
(9, 1, 10),
(10, 1, 11),
(11, 2, 6),
(12, 2, 7),
(13, 2, 8),
(14, 2, 9),
(15, 2, 10),
(16, 2, 11),
(17, 2, 12),
(18, 2, 13),
(19, 2, 14);

-- --------------------------------------------------------

--
-- Table structure for table `themes_sanction`
--

CREATE TABLE `themes_sanction` (
  `id` bigint NOT NULL,
  `libelle` varchar(255) NOT NULL,
  `duree` varchar(100) DEFAULT NULL,
  `complementaire` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `themes_sanction`
--

INSERT INTO `themes_sanction` (`id`, `libelle`, `duree`, `complementaire`) VALUES
(1, 'Emprisonnement', '3 ans', 0),
(3, 'Immobilisation', NULL, 0),
(4, 'Suspension du permis de conduire', '5 ans', 1),
(5, 'Annulation', '5 ans', 1),
(6, 'Peine de travail d\'intérêt général', NULL, 1),
(7, 'Peine de jours-amende', NULL, 1),
(8, 'Interdiction de conduire certains véhicules terrestres à moteur', '5 ans', 1),
(9, 'Obligation de stage de sensibilisation', NULL, 1),
(10, 'Interdiction de conduire un véhicule non-équipé d\'un EAD', '5 ans', 1),
(11, 'Confiscation du véhicule', NULL, 1),
(12, 'Emprisonnement', '2 ans', 0),
(13, 'Suspension du permis de conduire', '3 ans', 1),
(14, 'Annulation', '3 ans', 1);

-- --------------------------------------------------------

--
-- Table structure for table `themes_theme`
--

CREATE TABLE `themes_theme` (
  `id` bigint NOT NULL,
  `number` bigint UNSIGNED NOT NULL,
  `title` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `categorie_id` bigint DEFAULT NULL
) ;

--
-- Dumping data for table `themes_theme`
--

INSERT INTO `themes_theme` (`id`, `number`, `title`, `slug`, `categorie_id`) VALUES
(1, 1, 'Aide et assistance à la conduite: définition, rôle et homéostasie du risque', '1_aide-et-assistance', 1),
(2, 2, 'Alcool: diffusion et élimination', '2_alcool-diffusion-elimination', 8),
(3, 3, 'Alcool: effets et accidentologie', '3_alcool-effets-accidentologie', 8),
(4, 4, 'Alcool: évaluation du taux d\'alcool', '4_alcool_evaluation-taux', 8),
(5, 5, 'Alcool: le cadre réglementaire', '5_alcool-cadre-reglementaire', 8),
(6, 6, 'Assurance automobile (rôle, obligatoire et facultative)', '6_assurance-automobile', 5),
(7, 7, 'Circulation en hiver (conduite et préparation d\'un voyage)', '7_circulation-hiver', 4),
(8, 8, 'L\'âge et la conduite (classe d\'âge, sexe, risques)', '8_age-et-conduite', 7),
(9, 9, 'Approche multifactorielle de l\'accident (système HVEO)', '9_approche-multifactorielle-accident', 14),
(10, 10, 'L\'attention du conducteur (vigilance, attention et fatigue', '10_attention-conducteur', 13),
(11, 11, 'L\'autoroute', '11_autoroute', 4),
(12, 12, 'Eco-conduite', '12_eco-conduite', 17),
(13, 13, 'L\'utilisation rationnelle du véhicule (aspect mécanique)', '13_utilisation-rationnelle-vehicule', 1),
(14, 14, 'La communication entre les usagers de la route', '14_communication-usagers-route', 4),
(15, 15, 'La fonction sociale de la réglementation en matière de sécurité routière', '15_fonction-socilae-reglementation-sr', 5),
(16, 16, 'La physique appliquée au véhicule (identification et conséquences)', '16_physique-appliquee-vehicule', 1),
(17, 17, 'La vue du conducteur (fonctionnement de l\'oeil, tache de mariotte, champ visuel, réglementation', '17_vue-conduteur', 13),
(18, 18, 'Le comportement en cas d\'accident', '18_comportement-accident', 5),
(19, 19, 'Le constat amiable', '19_constat-amiable', 4),
(20, 20, 'Le continuum éducatif (formation obligatoire et facultative)', '20_continuum-educatif', 5),
(21, 21, 'Le partage social de la route avec les 2 roues et L5e', '21_partage-social-2-roues', 10),
(22, 22, 'Le partage sociale de la route avec les piétons', '22_partage-social-pietons', 10),
(23, 23, 'le permis à points (rôle et fonctionnement)', '23_pap', 3),
(24, 24, 'Le permis de conduire catégorie B (définition, conditions d\'obtention, probatoire)', '24_permis-B', 3),
(25, 25, 'Le risque routier chez les jeunes de 18 à 24 ans (probatoire, alcool, limitations)', '25_risque-routier-18-24', 7),
(26, 26, 'Le transport d\'une charge en sécurité à l\'aide d\'un véhicule', '25_transport-charge', 5),
(27, 27, 'Les croisements', '27_croisement', 4),
(28, 28, 'Les dépassements', '28_depassement', 4),
(29, 29, 'Les dispositifs de sécurité active (fonction à effet pervers)', '29_dispositif-securite-active', 2),
(30, 30, 'Les distances d\'arrêt', '30_distance_arret', 4),
(31, 31, 'Les documents et équipements obligatoires et facultatifs du véhicule', '31_doc_equipement_vehicule', 5),
(32, 32, 'Les ensembles de véhicules de la catégorie B (définition, condition d\'obtention, probatoire)', '32_ensemble_vehicule', 1),
(33, 33, 'Les feux obligatoires et facultatifs du véhicule', '33_feux_obligatoires_facultatifs', 1),
(34, 34, 'Les intersections gérées par la signalisation lumineuse', '34_intersections-gerees-signalisation-lumineuse', 4),
(35, 35, 'Les intersections non gérées par la signalisation lumineuse', '35_intersections-non-gerees-signalisation-lumineuse', 4),
(36, 36, 'Les justifications des politiques de sécurité routière', '36_justification-politiques-SR', 18),
(37, 37, 'Les pneus: adhérence, entretien, réglementation', '37_pneus', 1),
(38, 38, 'Les risques liés à la conduite de nuit', '38_conduite-de-nuit', 4),
(39, 39, 'Les risques liés à la conduite par intempérie', '39_conduite-intemperies', 14),
(40, 40, 'Les ronds-points et carrefour à sens giratoire', '40_carrefour-giratoire', 4),
(41, 41, 'Les substances psychoactives (sauf alcool)', '41_substances-psychoactives', 8),
(42, 42, 'Les systèmes de retenue: rôle, réglementation, accidentologie, installation des passagers', '42_systemes-retenues', 1),
(43, 43, 'Les usagers vulnérables', '43_usagers-vulnerables', 10),
(44, 44, 'Les véhicules d\'intérêt général', '44_VIG', 5),
(45, 45, 'Les vérifications de sécurité du véhicule', '45_verifications-securite-vehicule', 1),
(46, 46, 'Les voies réservées', '46_voies-reservees', 4),
(47, 47, 'Le partage social de la route avec les véhicules du groupe lours', '47_partage-social-groupe-lourd', 10),
(48, 48, 'Les passages à niveaux', '48_passages_niveaux', 4),
(49, 49, 'Pressions et influences incitant à une vitesse inadaptée', '49_vitesse-inadaptee', 9),
(50, 50, 'Le permis de conduire : sanctions administratives et pénales', '50_sanctions-permis', 3),
(51, 51, 'La signalisation horizontale', '51_signalisation-horizontale', 6),
(52, 52, 'La signalisation verticale', '52_signalisation-verticale', 6),
(53, 53, 'Stationnement - Arrêt - Immobilisation', '53_arret-stationnement', 4),
(54, 54, 'Surfaces vitrées et rétroviseurs : usagers, description, entretien', '54_surfaces-vitrees-retro', 1),
(55, 55, 'Temps de réaction et distances de sécurité', '55_TR-DS', 4),
(56, 56, 'Vitesse : la signalisation et son rôle', '56_vitesse-signalisation-role', 9),
(57, 57, 'Vitesse: réglementation et sanctions', '57_vitesse-reglementation-sanction', 9);

-- --------------------------------------------------------

--
-- Table structure for table `themes_theme_tags`
--

CREATE TABLE `themes_theme_tags` (
  `id` bigint NOT NULL,
  `theme_id` bigint NOT NULL,
  `categorie_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `themes_theme_tags`
--

INSERT INTO `themes_theme_tags` (`id`, `theme_id`, `categorie_id`) VALUES
(1, 1, 2),
(2, 2, 12),
(3, 2, 13),
(5, 3, 11),
(6, 3, 12),
(7, 3, 14),
(8, 3, 15),
(11, 4, 5),
(10, 4, 12),
(9, 4, 13),
(14, 5, 3),
(16, 5, 5),
(15, 5, 12),
(13, 5, 16),
(18, 6, 1),
(19, 6, 5),
(17, 6, 16),
(20, 7, 1),
(21, 7, 4),
(22, 7, 5),
(23, 7, 14),
(24, 8, 3),
(25, 8, 7),
(26, 8, 8),
(27, 8, 14),
(28, 8, 15),
(29, 9, 4),
(32, 9, 7),
(31, 9, 14),
(30, 9, 15),
(35, 10, 7),
(33, 10, 13),
(34, 10, 14),
(37, 11, 5),
(38, 11, 6),
(36, 11, 9),
(39, 11, 14),
(40, 12, 1),
(41, 12, 2),
(42, 12, 4),
(43, 12, 5),
(44, 12, 6),
(45, 13, 1),
(46, 13, 2),
(47, 13, 4),
(48, 13, 17),
(49, 14, 1),
(50, 14, 4),
(51, 14, 5),
(52, 14, 7),
(53, 14, 10),
(55, 15, 5),
(56, 15, 7),
(54, 15, 16),
(57, 16, 1),
(59, 16, 9),
(58, 16, 11),
(60, 17, 5),
(61, 17, 7),
(62, 17, 11),
(63, 17, 13),
(64, 17, 14),
(65, 18, 4),
(66, 18, 5),
(67, 18, 6),
(68, 18, 7),
(69, 18, 14),
(70, 19, 1),
(71, 19, 5),
(72, 19, 7),
(73, 20, 3),
(74, 20, 5),
(75, 20, 7),
(76, 21, 4),
(77, 21, 5),
(78, 21, 6),
(79, 21, 10),
(80, 21, 14),
(81, 22, 4),
(82, 22, 5),
(83, 22, 6),
(84, 22, 7),
(85, 22, 10),
(86, 22, 14),
(88, 23, 3),
(89, 23, 5),
(87, 23, 16),
(91, 24, 3),
(92, 24, 5),
(90, 24, 16),
(93, 25, 7),
(94, 25, 8),
(95, 25, 9),
(96, 25, 12),
(97, 25, 14),
(98, 26, 1),
(99, 26, 4),
(100, 26, 5),
(101, 26, 14),
(102, 26, 16),
(103, 27, 4),
(104, 27, 5),
(105, 27, 6),
(106, 27, 14),
(107, 27, 16),
(108, 28, 4),
(109, 28, 5),
(110, 28, 6),
(111, 28, 14),
(112, 28, 16),
(113, 29, 1),
(114, 29, 2),
(115, 29, 4),
(116, 29, 14),
(117, 30, 1),
(118, 30, 2),
(119, 30, 4),
(120, 30, 9),
(121, 30, 11),
(122, 31, 1),
(123, 31, 3),
(124, 31, 4),
(125, 31, 5),
(126, 31, 7),
(127, 31, 16),
(128, 32, 1),
(129, 32, 3),
(130, 32, 4),
(131, 32, 5),
(132, 32, 6),
(133, 32, 9),
(134, 33, 1),
(135, 33, 2),
(136, 33, 4),
(137, 33, 5),
(138, 33, 16),
(140, 34, 4),
(141, 34, 5),
(142, 34, 6),
(139, 34, 16),
(144, 35, 4),
(145, 35, 5),
(146, 35, 6),
(143, 35, 16),
(148, 36, 5),
(149, 36, 7),
(147, 36, 18),
(150, 37, 1),
(151, 37, 2),
(152, 37, 5),
(153, 37, 14),
(154, 38, 4),
(155, 38, 5),
(156, 38, 6),
(157, 38, 7),
(158, 38, 14),
(159, 38, 17),
(160, 39, 1),
(161, 39, 4),
(162, 39, 5),
(163, 39, 7),
(164, 39, 14),
(165, 39, 17),
(166, 40, 4),
(167, 40, 5),
(168, 40, 6),
(169, 41, 5),
(170, 41, 7),
(171, 41, 8),
(172, 41, 13),
(173, 41, 14),
(174, 41, 16),
(175, 41, 18),
(176, 42, 1),
(177, 42, 2),
(178, 42, 5),
(179, 42, 11),
(180, 42, 14),
(182, 43, 4),
(184, 43, 7),
(181, 43, 10),
(183, 43, 14),
(185, 44, 1),
(186, 44, 4),
(187, 44, 5),
(188, 44, 6),
(189, 44, 9),
(190, 44, 10),
(191, 45, 1),
(192, 45, 2),
(193, 45, 5),
(194, 45, 17),
(195, 46, 1),
(196, 46, 4),
(197, 46, 5),
(198, 46, 6),
(199, 47, 1),
(200, 47, 4),
(201, 47, 5),
(202, 47, 6),
(203, 47, 10),
(204, 48, 4),
(205, 48, 5),
(206, 48, 6),
(207, 48, 14),
(208, 49, 5),
(209, 49, 7),
(210, 49, 9),
(211, 49, 14),
(212, 49, 16),
(215, 50, 3),
(216, 50, 5),
(213, 50, 16),
(214, 50, 18),
(217, 51, 4),
(218, 51, 5),
(219, 51, 6),
(220, 51, 9),
(221, 51, 16),
(223, 52, 4),
(224, 52, 5),
(225, 52, 6),
(222, 52, 16),
(226, 53, 1),
(227, 53, 4),
(228, 53, 5),
(229, 53, 6),
(230, 53, 14),
(231, 53, 16),
(232, 54, 1),
(233, 54, 2),
(234, 54, 4),
(235, 54, 5),
(236, 55, 1),
(237, 55, 4),
(238, 55, 5),
(239, 55, 7),
(240, 56, 4),
(241, 56, 5),
(242, 56, 6),
(243, 56, 9),
(244, 56, 16),
(247, 57, 4),
(248, 57, 5),
(246, 57, 9),
(245, 57, 16);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `eleves_eleve`
--
ALTER TABLE `eleves_eleve`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `eleves_progression`
--
ALTER TABLE `eleves_progression`
  ADD PRIMARY KEY (`id`),
  ADD KEY `eleves_progression_eleve_id_936361a7_fk_eleves_eleve_id` (`eleve_id`);

--
-- Indexes for table `themes_categorie`
--
ALTER TABLE `themes_categorie`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `themes_contentblock`
--
ALTER TABLE `themes_contentblock`
  ADD PRIMARY KEY (`id`),
  ADD KEY `themes_contentblock_theme_id_850bb4bf_fk_themes_theme_id` (`theme_id`);

--
-- Indexes for table `themes_reglementation`
--
ALTER TABLE `themes_reglementation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `themes_reglementation_theme_id_3ec9002e_fk_themes_theme_id` (`theme_id`);

--
-- Indexes for table `themes_reglementation_sanctions`
--
ALTER TABLE `themes_reglementation_sanctions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `themes_reglementation_sa_reglementation_id_sancti_0f0b9839_uniq` (`reglementation_id`,`sanction_id`),
  ADD KEY `themes_reglementatio_sanction_id_5b2beecd_fk_themes_sa` (`sanction_id`);

--
-- Indexes for table `themes_sanction`
--
ALTER TABLE `themes_sanction`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `themes_theme`
--
ALTER TABLE `themes_theme`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `number` (`number`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `themes_theme_categorie_id_faa49949_fk_themes_categorie_id` (`categorie_id`);

--
-- Indexes for table `themes_theme_tags`
--
ALTER TABLE `themes_theme_tags`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `themes_theme_tags_theme_id_categorie_id_6a48180b_uniq` (`theme_id`,`categorie_id`),
  ADD KEY `themes_theme_tags_categorie_id_6e13bbf4_fk_themes_categorie_id` (`categorie_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `eleves_eleve`
--
ALTER TABLE `eleves_eleve`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `eleves_progression`
--
ALTER TABLE `eleves_progression`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT for table `themes_categorie`
--
ALTER TABLE `themes_categorie`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `themes_contentblock`
--
ALTER TABLE `themes_contentblock`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `themes_reglementation`
--
ALTER TABLE `themes_reglementation`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `themes_reglementation_sanctions`
--
ALTER TABLE `themes_reglementation_sanctions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `themes_sanction`
--
ALTER TABLE `themes_sanction`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `themes_theme`
--
ALTER TABLE `themes_theme`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `themes_theme_tags`
--
ALTER TABLE `themes_theme_tags`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=249;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `eleves_progression`
--
ALTER TABLE `eleves_progression`
  ADD CONSTRAINT `eleves_progression_eleve_id_936361a7_fk_eleves_eleve_id` FOREIGN KEY (`eleve_id`) REFERENCES `eleves_eleve` (`id`);

--
-- Constraints for table `themes_contentblock`
--
ALTER TABLE `themes_contentblock`
  ADD CONSTRAINT `themes_contentblock_theme_id_850bb4bf_fk_themes_theme_id` FOREIGN KEY (`theme_id`) REFERENCES `themes_theme` (`id`);

--
-- Constraints for table `themes_reglementation`
--
ALTER TABLE `themes_reglementation`
  ADD CONSTRAINT `themes_reglementation_theme_id_3ec9002e_fk_themes_theme_id` FOREIGN KEY (`theme_id`) REFERENCES `themes_theme` (`id`);

--
-- Constraints for table `themes_reglementation_sanctions`
--
ALTER TABLE `themes_reglementation_sanctions`
  ADD CONSTRAINT `themes_reglementatio_reglementation_id_486fdbf0_fk_themes_re` FOREIGN KEY (`reglementation_id`) REFERENCES `themes_reglementation` (`id`),
  ADD CONSTRAINT `themes_reglementatio_sanction_id_5b2beecd_fk_themes_sa` FOREIGN KEY (`sanction_id`) REFERENCES `themes_sanction` (`id`);

--
-- Constraints for table `themes_theme`
--
ALTER TABLE `themes_theme`
  ADD CONSTRAINT `themes_theme_categorie_id_faa49949_fk_themes_categorie_id` FOREIGN KEY (`categorie_id`) REFERENCES `themes_categorie` (`id`);

--
-- Constraints for table `themes_theme_tags`
--
ALTER TABLE `themes_theme_tags`
  ADD CONSTRAINT `themes_theme_tags_categorie_id_6e13bbf4_fk_themes_categorie_id` FOREIGN KEY (`categorie_id`) REFERENCES `themes_categorie` (`id`),
  ADD CONSTRAINT `themes_theme_tags_theme_id_9bf3b86f_fk_themes_theme_id` FOREIGN KEY (`theme_id`) REFERENCES `themes_theme` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
