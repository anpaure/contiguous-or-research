# The \(D_4\) fringe bank versus the canonical \(V_4\) component

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let \(F_4\) be the canonical MSW \(D_4\)-port factor and let \(G_4\) be
the non-coordinate fourteen-row factor with first-insertion pair totals

\[
                         (5,5,2,2)\longrightarrow(5,5,1,3).       \tag{0.1}
\]

There are three exact conclusions.

1. The ownership overlay of \(F_4\) and \(G_4\) is connected already on
   its \(X\)-state edges. Thus the fourteen-for-fourteen replacement is
   one indivisible ownership component. It has no proper component packets.
2. Strict fringe deployment nevertheless gives many independent legal
   whole packets. All but an exponentially small fraction of the \(C_s\)
   Dyck roots split into disjoint common-context classes of fourteen, and
   either \(F_4\) or \(G_4\) may be installed independently in every class.
3. This is owner coverage, not coverage of the four \(V_4\) target cells.
   Every such fringe replacement lies strictly inside the free Dyck filling
   of the endpoint window and fixes the filling's complementary exported
   ports. The matched target contains both local ports, so the replacement
   is erased. The dense fringe bit has zero action on the endpoint cell
   carrying the \(C_s\) plateau.

Accordingly the non-coordinate factor does not fragment the fixed canonical
\(V_4\) overlay. Adding a shore to a connected ownership graph cannot
disconnect it. Recomputing the \(V_4\) overlay after first decorating the
seed is a different construction and remains unproved.

There is a small exact parent-aligned bank. Initial or terminal
concatenation copies cover

\[
                         14C_{s-4}
      =\left(\frac7{128}+o(1)\right)C_s               \tag{0.2}
\]

roots at one boundary. Requiring simultaneous initial and terminal
\(D_4\) blocks gives legal four-state product packets on

\[
                         196C_{s-8}
      =\left(\frac{49}{16384}+o(1)\right)C_s           \tag{0.3}
\]

roots. Across the four Catalan families of total size

\[
                         M_s=C_s+2C_{s-1}+C_{s-2},      \tag{0.4}
\]

the same asymptotic fraction \(49/16384\) is covered. This is far from
the \(1-o(1)\) occurrence coverage required by the discrepancy theorem.
Moreover the fourteen rows have heterogeneous old/new labels, so even a
legal whole-packet state is not one uniform Boolean target bit.

Thus the strengthened canonical no-go survives the currently proved
\(D_4\) deployment. The exact missing object is an occurrence-resolved,
parent-aligned \(D_4\) atlas covering all but \(o(M_s)\) occurrences with
independently selectable joint states. No such atlas, and no invariant
excluding every possible such atlas, is presently proved.

## 1. The canonical four-family component

Take as input the proved canonical \(V_4\) statement. The two endpoint
coordinate swaps generate one ownership component containing the four
root families

\[
             \Omega_{00},\Omega_{10},\Omega_{01},\Omega_{11}       \tag{1.1}
\]

of respective sizes

\[
                         C_s,\qquad C_{s-1},\qquad
                         C_{s-1},\qquad C_{s-2}.         \tag{1.2}
\]

Choosing a coordinate shore only permutes their four physical cells.
In particular the largest cell remains at least \(C_s\), independently of
the fact that their total \(M_s\) may be at most \(4p\). The abstract
two-partition discrepancy signing is therefore not implemented by the
canonical coordinate overlay: it has one component variable, not bounded
independent block variables.

The question is whether \(G_4\) supplies the missing variables.

## 2. The local \(F_4\)-\(G_4\) overlay is connected

Label the fourteen ports

\[
\begin{array}{lllllll}
 A=1234,&B=1235,&C=1236,&D=1237,&E=1245,&F=1246,&G=1247,\\
 H=1256,&I=1257,&J=1345,&K=1346,&L=1347,&M=1356,&N=1357.
\end{array}                                             \tag{2.1}
\]

Form the bipartite ownership overlay of the two local factors, using both
the \(X\)-states and adjacent-union colours. The common port \(P\) joins
the \(F_4\)-row and \(G_4\)-row rooted at \(P\). Contract these fourteen
port edges. If an internal state in the \(G_4\)-row \(P\) is owned by the
\(F_4\)-row \(Q\), the contracted graph has an edge \(P-Q\).

### Theorem 2.1 (local indivisibility)

The contracted \(X\)-state graph contains the following spanning tree:

\[
\begin{array}{c|c@{\qquad}c|c}
\text{edge}&\text{shared state}&\text{edge}&\text{shared state}\\ \hline
A-C&1238&B-C&1378\\
B-E&1678&C-G&1267\\
C-D&1467&D-F&1278\\
E-J&2345&E-H&3456\\
F-K&2346&G-L&2347\\
H-I&3467&I-N&2357\\
J-M&2456&&
\end{array}                                             \tag{2.2}
\]

Consequently the full ownership overlay has one component, with fourteen
rows on either shore.

#### Proof

Every state in the middle columns of (2.2) occurs in the displayed
\(G_4\)-row and in the canonical \(F_4\)-row named by the other endpoint.
For example, \(1238\) is internal to the new row \(A\) and to the old row
\(C\), while \(2345\) is internal to the new row \(E\) and the old row
\(J\). All incidences follow by literal reading of the two path tables.

The thirteen edges connect all fourteen vertices: from \(A\) one reaches
\(C\), then \(B,D,G\), then \(E,F,L\), then \(H,J,K\), and finally
\(I,M,N\). Thus the contracted \(X\)-subgraph is connected. Adding the
\(Y\)-colour edges cannot disconnect it. Undoing the port contractions
proves that the bipartite overlay has one component. \(\square\)

### Corollary 2.2

The direct \(F_4\)-versus-\(G_4\) switching cube has dimension one. Its
only factors are the two complete shores. In particular the non-coordinate
primitive does not itself split into smaller independently assignable
root packets.

The statement remains true after a common coordinate relabelling. Also,
augmenting a fixed connected \(V_4\) ownership graph by adding \(G_4\)
rows or incidences cannot fragment the old component: the old connected
graph remains a subgraph. A possible fragmentation theorem must first
replace the seed and then recompute its coordinate overlays; it cannot be
obtained merely by adding the \(G_4\) shore to the canonical overlay.

There is a finite whole-block library. The group

\[
 H_4=\langle(2\,3),(4\,5),(6\,7)\rangle\cong C_2^3      \tag{2.3}
\]

preserves \(D_4\), so \(F_4\) and every reindexed factor \(hG_4\),
\(h\in H_4\), are legal states on the same fourteen ports. These are
multi-state choices only at whole-block scale. Every \(hG_4\) still has
pair totals \((5,5,1,3)\), because \(H_4\) only reverses labels inside the
three active pairs. Thus the pair-class menu has only the two profiles
\((5,5,2,2)\) and \((5,5,1,3)\), and Theorem 2.1 supplies no independent
subchoices inside either profile.

## 3. Exact dense owner packetization

Identify \(D_s\) with ordered binary trees having \(s\) nodes. Let \(a_s\)
be the number of trees containing no fringe subtree of size four. For a
nonavoiding tree choose its first size-four fringe subtree in preorder.
Deleting that subtree leaves a one-hole tree context \(C[\,]\). Replacing
the hole by any \(P\in D_4\) neither moves the hole nor creates an earlier
size-four fringe root. Hence

\[
                         \mathcal K_C=\{C[P]:P\in D_4\}              \tag{3.1}
\]

is a well-defined class of fourteen roots, and these classes partition
the nonavoiding roots.

### Theorem 3.1 (dense independent whole packets)

For every class \(\mathcal K_C\), the common-context lift of either \(F_4\)
or \(G_4\) is a legal exact replacement on those fourteen rows. Choices
on distinct classes are independent. The number of packets is

\[
                         P_s=\frac{C_s-a_s}{14}.          \tag{3.2}
\]

Moreover \(a_s/C_s=o(1)\) exponentially.

#### Proof

Both local factors own every \(4\)-state and every adjacent \(5\)-union
exactly once and have the same rooted complementary ports. The anchored
context-substitution theorem therefore lifts either complete local ledger
through the fixed context \(C[\,]\). Its fourteen global rows replace the
same global state and colour multisets, so the replacement is exact.
Different classes have disjoint row-root supports, and each replacement
balances its own two ledgers; arbitrary class choices are therefore legal.

The avoidance generating function is

\[
                         A(z)=1+zA(z)^2-14z^4,           \tag{3.3}
\]

and hence

\[
                         A(z)=\frac{1-\sqrt{1-4z+56z^5}}{2z}.       \tag{3.4}
\]

The radicand equals \(7/128\) at \(z=1/4\). Its derivative is
\(-4+280z^4<0\) on \([0,1/4]\), so it is decreasing and positive
throughout that interval. Thus \(A\) is analytic past \(1/4\). Since its
coefficients are nonnegative, Pringsheim's theorem gives a radius strictly
larger than \(1/4\). Therefore \(a_s=O(\rho^{-s})\) for some
\(\rho>1/4\), whereas \(C_s=\Theta(4^ss^{-3/2})\). This proves the
exponential ratio claim. \(\square\)

By Theorem 2.1, every class in Theorem 3.1 is one atomic fourteen-row
binary block; the context does not reveal smaller overlay components.

Applying the same construction separately to the four free fillings of
sizes \(s,s-1,s-1,s-2\) gives owner coverage

\[
 M_s-R_s,\qquad
 R_s=a_s+2a_{s-1}+a_{s-2}=o(M_s),                     \tag{3.5}
\]

by packets of size fourteen. Thus the owner-coverage part of the abstract
discrepancy hypothesis really does hold.

## 4. Owner coverage is not \(V_4\)-action coverage

Every packet in Section 3 is a substitution in a strict fringe hole of the
free filling. It fixes that hole's two complementary ports. Each of the
four \(V_4\) endpoint occurrences contains the complete free-filling slab,
and hence contains both ports of every strict fringe hole used in (3.1).

### Theorem 4.1 (fringe-bit erasure on the four cells)

The local contribution of a packet in Section 3 to any of the four matched
endpoint targets is independent of the choice \(F_4\) or \(G_4\). Thus the
dense packet bit has zero projection to the \(V_4\) cell label.

#### Proof

Let \(P\) and \(J\setminus P\) be the two local ports of the chosen fringe
hole. The matched endpoint target is an intersection containing both
states. Its restriction to the fringe coordinates is contained in

\[
                         P\cap(J\setminus P)=\varnothing.           \tag{4.1}
\]

All exterior coordinates are fixed by the common context. Therefore the
physical target is unchanged by every internal state of the local factor.
The same proof applies in each of the four families: their differences are
the two outer boundary atoms, not the strict internal filling. \(\square\)

The union dual is equally rigid, because the local contribution is always
\(P\cup(J\setminus P)=J\).

Consequently (3.5) cannot be inserted as the exceptional-set estimate in
the four-cell discrepancy theorem. That theorem needs occurrences which
receive two physical endpoint labels. The packets in Section 3 assign
factor states to almost every owner, but assign no new \(V_4\) endpoint
label to those owners. In the relevant target projection their effective
exceptional set is still all of \(\Omega\).

This also explains the apparent conflict with the local pair bridge (0.1).
The bridge moves a window whose boundary cuts the \(D_4\) slab. A larger
matched window containing the entire fringe slab erases it.

## 5. What the literal parent-aligned bank covers

The simplest way to keep the \(D_4\) action visible is to place its block at
an endpoint of the flip word rather than in a strict fringe hole.

### Proposition 5.1 (one active boundary)

For every \(R\in D_{s-4}\), the roots

\[
                         \{PR:P\in D_4\}                \tag{5.1}
\]

form one legal fourteen-row initial-boundary packet. Arbitrary choices of
\(F_4\) or \(G_4\) on these packets are exact. Their root supports are
disjoint, and their union has size

\[
                         14C_{s-4}
   =\left(\frac7{128}+o(1)\right)C_s.                  \tag{5.2}
\]

#### Proof

The MSW concatenation law gives

\[
                         \rho(PR)=\rho(P)\mathbin\Vert
                                      (8+\rho(R)).       \tag{5.3}
\]

Thus the first four local exchanges form one common \(D_4\)-port hole and
the suffix context is the same for all \(P\). The complete \(X/Y\) ledger
of either local factor lifts through that suffix, proving legality. The
suffix \(R\) is uniquely recovered from the root, so the packet supports
are disjoint. Counting gives \(14C_{s-4}\), and the Catalan ratio tends to
\(14/4^4=7/128\). \(\square\)

There is a symmetric terminal-boundary bank of the same size.

The block count in (5.2) is not the count of nontrivially labelled
occurrences. Comparing the first-insertion columns of the two local factors,
the roots

\[
                         1234,\qquad1235,\qquad1356      \tag{5.4}
\]

have the same old and new label. The other eleven roots change label.
Thus this literal one-boundary bank gives a nonconstant marked bit on
exactly

\[
                         11C_{s-4}                      \tag{5.5}
\]

root occurrences. The remaining three rows in every packet are inert in
this projection.

### Proposition 5.2 (two-boundary four-state product blocks)

For every \(U\in D_{s-8}\), the root block

\[
                 \mathcal B_U=\{PUQ:P,Q\in D_4\}       \tag{5.6}
\]

has \(196\) rows and admits the four independent exact states

\[
                     (F_4,F_4),\quad(F_4,G_4),\quad
                     (G_4,F_4),\quad(G_4,G_4).          \tag{5.7}
\]

The blocks are disjoint and cover

\[
                         196C_{s-8}
   =\left(\frac{49}{16384}+o(1)\right)C_s              \tag{5.8}
\]

roots.

#### Proof

The initial and terminal \(D_4\) exchange blocks in \(PUQ\) are disjoint.
Fixing \(U\), the two complete local ledgers tensor through the common
middle context. Replacing either local factor preserves its own state and
colour multisets, so the two choices commute and all four combinations are
exact. The decomposition \(P|U|Q\) is unique, giving disjoint blocks.
Counting and the Catalan ratio give (5.8). \(\square\)

Only the \(11^2=121\) rows for which both local roots avoid the inert list
(5.4) can receive two nonconstant bits. Hence even before asking that the
two changed coordinate pairs be common and disjoint, the number of
potentially nondegenerate four-state occurrences is at most

\[
                         121C_{s-8}.                    \tag{5.9}
\]

Applying Proposition 5.2 to the four free-filling sizes gives total
two-boundary coverage

\[
 196\bigl(C_{s-8}+2C_{s-9}+C_{s-10}\bigr).             \tag{5.10}
\]

Since \(M_s/C_s\to25/16\), division by (0.4) yields

\[
 \frac{196(C_{s-8}+2C_{s-9}+C_{s-10})}{M_s}
               \longrightarrow\frac{196}{4^8}
               =\frac{49}{16384}.                     \tag{5.11}
\]

Thus the certified literal four-state atlas leaves

\[
             \left(1-\frac{49}{16384}+o(1)\right)M_s  \tag{5.12}
\]

occurrences outside its blocks. This is not an admissible exceptional set:
it is \(\Theta(p)\), whereas the discrepancy gate requires \(o(p/s)\).

Proposition 5.2 asserts four legal factor states. It does not assert that
all 196 rows see the same four physical targets. The rowwise
first-insertion transitions of \(F_4\to G_4\) are heterogeneous; only
selected rows realize, for example, the literal pairs \(4\to7\) and
\(2\to6\). Hence occurrence-resolved four-target action is a further
condition even on the covered blocks.

## 6. The exact remaining distinction

There are two meanings of the assertion that the \(D_4\) factor fragments
the \(V_4\) component.

1. Augment the canonical overlay by a \(G_4\) shore. This cannot fragment
   anything: a connected graph remains connected after vertices and edges
   are added. Theorem 2.1 shows that the new local shore itself attaches as
   one whole component.
2. First decorate the seed by independent \(D_4\) replacements, then
   recompute its two endpoint coordinate overlays. This is not the same
   graph. Its component structure is not determined by Theorem 2.1. A
   positive result would require the phase-owner permutations of the
   decorated factor and a proof that their orbits have bounded size on
   \(M_s-o(M_s)\) occurrences.

The dense decoration of Section 3 supplies many legal seed factors, but its
direct \(V_4\)-target projection is zero by Theorem 4.1. No theorem yet
shows that recomputing coordinate overlays after those decorations produces
the required bounded components. Conversely, local connectedness alone
does not prove that every recomputed overlay stays connected.

The exact surviving gate is:

> Construct a parent-aligned atlas whose joint ownership atoms have
> \(O(1)\) or \(o(p/s^2)\) occurrence size, cover
> \(M_s-o(p/s)\) endpoint occurrences, admit at least four legal joint
> states, and send those states to the required distinct physical target
> cells; or prove that every decorated endpoint overlay retains a component
> of \(\Omega(C_s)\) occurrences.

The present \(D_4\) fringe theorem proves neither alternative. What it
does prove exactly is the separation between legal owner packetization and
physical endpoint packetization, and the fourteen-row indivisibility of
the available non-coordinate primitive.
