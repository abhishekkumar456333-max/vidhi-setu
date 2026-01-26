import React from "react";
import { cn } from "../../lib/utils";
import { motion } from "framer-motion";

export const BentoGrid = ({ className, children }) => {
  return (
    <div
      className={cn(
        "grid grid-cols-1 md:grid-cols-3 gap-4 max-w-7xl mx-auto",
        className
      )}
    >
      {children}
    </div>
  );
};

export const BentoGridItem = ({
  className,
  title,
  description,
  header,
  icon,
}) => {
  return (
    <motion.div
      whileHover={{ y: -5, scale: 1.01 }}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}
      className={cn(
        "row-span-1 rounded-xl group/bento hover:shadow-2xl transition duration-200 shadow-sm p-5 bg-white border border-zinc-100 justify-between flex flex-col space-y-4",
        className
      )}
    >
      {header}
      <div className="group-hover/bento:translate-x-2 transition duration-200">
        {icon}
        <div className="font-sans font-bold text-zinc-800 mb-2 mt-2">
          {title}
        </div>
        <div className="font-sans font-normal text-zinc-500 text-xs leading-relaxed">
          {description}
        </div>
      </div>
    </motion.div>
  );
};
