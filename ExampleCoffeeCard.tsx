import styles from './example.module.scss';

interface CoffeeCardData {
  title: string;
  description: string[];
  price: number;
}

export const ExampleCoffeeCard: React.FC<{
  coffeeCardData: CoffeeCardData;
}> = ({ coffeeCardData }) => {
  return (
    <div className={styles.rowContainer}>
      <div className={styles.title}>{coffeeCardData.title}</div>
      <div className={styles.info}>
        {coffeeCardData.map((text) => {
          return <div className={styles.bulletPoint}>{text}</div>;
        })}
      </div>
      <div className={styles.price}>{coffeeCardData.price}</div>
    </div>
  );
};
