# The odd beta charge closes on the native connector lattice

**Date:** 2026-08-06  
**Method:** exact five-coordinate physical/matching paths; no computation
or search  
**Status:** independently audited local theorem. It avoids the
scan-pair/head alignment premise entirely: pair the first connector with
one connector-lattice head \(02\), keep a second head fixed, and convert
the first two connectors in place. The three endpoints have the uniform
form \(C^*(a_1)|C(a_1)|H\).
The literal paths are independently replayed in Section 10 of
MATH_AUDIT_ODD_FULL_MATCHING_BETA_AND_TAGGED_RETURN_20260806.md.

## 1. Geometry and the fixed connector head

Use the physical order

\[
                          g\mid b\mid v\mid u\mid w.
\tag{1.1}
\]

The first selected scan pair and first two connector blocks are

\[
 p_1=(g,b),\qquad C_1=(b,v),\qquad C_2=(u,w).
\tag{1.2}
\]

Here \(b=B_1\), \(v=G_1^*\), and \(C_2\) is the nearer member of a
connector-lattice double head

\[
                         C_2|C_3=H|H,\qquad H=02,
\tag{1.3}
\]

temporarily placed immediately after \(C_1\). The farther \(C_3\) is fixed
through every local path and is an occurrence marker. The setup half has already
written \(G_1^*=2-B_1\), so

\[
 C_1=\begin{cases}
 02,&a_1=0,\\
 20,&a_1=1,2.
 \end{cases}
\tag{1.4}
\]

No opposite source connector is needed. The local conversion will write
\(C^*(a_1)\) at \(C_1\) and a preserved copy \(C(a_1)\) at \(C_2\).

At every physical endpoint below, \(p_1\) is one of the six selected
nonquiet states. Hence its matching edge is forced before any later scan
pair can act.

## 2. The \(a_1=0\) connector pair

The source and target are

\[
 \begin{aligned}
 10202
   &\quad(C_1=02,\ C_2=02,\ p_1=10),\\
 12200
   &\quad(C_1=22,\ C_2=00,\ p_1=12).
 \end{aligned}
\tag{2.1}
\]

Thus the endpoint connectors are exactly

\[
                 C^*(0)=22,\qquad C^*(2)=00.
\]

The literal directed path is

\[
\begin{array}{rclcl}
10202&\xrightarrow{\,w\to u\,}&10211
     &\xrightarrow{\,10\to01\text{ on }p_1\,}&01211,\\
01211&\xrightarrow{\,v\to b\,}&02111
     &\xrightarrow{\,02\to11\text{ on }p_1\,}&11111,\\
11111&\xrightarrow{\,u\to v\,}&11201
     &\xrightarrow{\,11\to02\text{ on }p_1\,}&02201,\\
02201&\xrightarrow{\,w\to u\,}&02210
     &\xrightarrow{\,02\to11\text{ on }p_1\,}&11210,\\
11210&\xrightarrow{\,v\to b\,}&12110
     &\xrightarrow{\,12\to21\text{ on }p_1\,}&21110,\\
21110&\xrightarrow{\,u\to v\,}&21200
     &\xrightarrow{\,21\to12\text{ on }p_1\,}&12200.
\end{array}
\tag{2.2}
\]

Every physical arrow is an adjacent unit transfer in (1.1); every second
arrow is the forced row of \(p_1\).

## 3. The \(a_1=2\) connector pair

Now

\[
 12002
   \quad(C_1=20,\ C_2=02,\ p_1=12)
\]

must become

\[
 10022
   \quad(C_1=00,\ C_2=22,\ p_1=10).
\]

These are \(C^*(2)\) and \(C^*(0)\). The exact path is

\[
\begin{array}{rclcl}
12002&\xrightarrow{\,b\to v\,}&11102
     &\xrightarrow{\,11\to02\text{ on }p_1\,}&02102,\\
02102&\xrightarrow{\,v\to u\,}&02012
     &\xrightarrow{\,02\to11\text{ on }p_1\,}&11012,\\
11012&\xrightarrow{\,b\to v\,}&10112
     &\xrightarrow{\,10\to01\text{ on }p_1\,}&01112,\\
01112&\xrightarrow{\,v\to u\,}&01022
     &\xrightarrow{\,01\to10\text{ on }p_1\,}&10022.
\end{array}
\tag{3.1}
\]

Again \(p_1\) is nonquiet at every physical endpoint.

## 4. The optional neutral copy

For \(a_1=1\), \(C_1=20=C^*(1)\) is already final. If a neutral target
occurrence is to receive the head copy, the two-step path

\[
\begin{array}{rclcl}
12002&\xrightarrow{\,w\to u\,}&12011
     &\xrightarrow{\,12\to21\text{ on }p_1\,}&21011,\\
21011&\xrightarrow{\,w\to u\,}&21020
     &\xrightarrow{\,21\to12\text{ on }p_1\,}&12020
\end{array}
\tag{4.1}
\]

writes \(C_2=20=C(1)\) and restores \(C_1\) and \(p_1\). If no such
neutral occurrence is being assigned, omit the beta operation entirely.

## 5. Exact local theorem

### Theorem 5.1 (connector-lattice beta pair)

For \(a_1=0\) or \(2\), one connector-lattice head at \(C_2=02\) gives a
directed path which simultaneously:

1. changes the mixed first connector \(C_1\) to \(C^*(a_1)\);
2. changes \(C_2\) to
   \[
                     C(a_1)=C^*(2-a_1);
   \]
3. changes \(B_1\) to \(B_1^*\);
4. ends at the literal target endpoint of \(p_1\); and
5. never selects a later scan pair.

For \(a_1=1\), the first connector is already final; the optional path
(4.1) writes the same uniform copy \(C_2=C(a_1)\).

#### Proof

Equations (2.2), (3.1), and (4.1) enumerate all physical and forced
matching edges. Their endpoints have the connector values stated above.
Every physical endpoint has nonquiet \(p_1\), so the following matching
edge is forced there. The majority and minority states displayed in each
branch are pairwise distinct, making each route simple.

The two nontrivial branches have the same total mass, so the retained
collar/residual signed record is still needed to distinguish them. That
record already recovers \(a_1\) from the residual charge and collar data.
With it fixed, the two paths are occurrence-disjoint. \(\square\)

## 6. Consequence and exact remaining interface

The local beta problem no longer requires:

- moving a connector-aligned head onto the offset scan-pair lattice;
- making \(p_1\) quiet;
- preparing an external relay clock; or
- a root/endpoint parity register.

For \(a_1=0,2\), global charge guarantees that the unfinished bank contains
at least one opposite source digit \(2-a_1\). Its target connector is
\(C^*(2-a_1)=C(a_1)\), exactly the copy written at \(C_2\). The remaining
physical task is therefore the ordinary connector-lattice occurrence
transport:

1. retain the source address of one opposite target occurrence;
2. move the connector double head so its nearer member occupies \(C_2\);
3. apply Theorem 5.1; and
4. return the completed copy \(C(a_1)\) to the selected target address,
   with the farther \(H\) as a fixed occurrence marker, restoring every
   crossed connector.

This is exactly the marked connector shuttle already used for the other
bounded residual pairs, except that its
local conversion is now (2.2) or (3.1). A fixed second head or stationary
marked corridor must still supply the occurrence decoder during transport;
scalar reachability alone is not enough. The ordered collar source must
also remain recorded until the target collar is literal; the copy
\(C(a_1)\) records \(a_1\), not the order of the separate collar digits.
