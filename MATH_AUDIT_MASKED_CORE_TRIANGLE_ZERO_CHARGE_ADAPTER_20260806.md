# Independent audit of the masked-core zero-charge adapter

## Verdict

The masked-core triangle is a valid bounded-support, zero-source-charge
adapter between different invariant-core fibres.  It closes the local
obstruction isolated in
`MATH_THEOREM_C6_CORE_FIBRE_INVARIANCE_AND_GLOBAL_CONNECTIVITY_GATE_20260806.md`.

For one application it preserves, literally and address by address,

* every protected crossing source-union value;
* the complete immediate-root, owner, and immediate-upper rows;
* every occurrence ticket attached to those addresses;
* source length and component parity; and
* the owner-phase residence floor.

It also gives an exact elementary core mutation

\[
 (K,F,U;x)\longmapsto (K-u+y,F,U-y+u;x),               \tag{0.1}
\]

where `u in K`, the cut marker `x in F`, and `y in U`.  Thus the core
exchange keeps both the moving bank and the distinguished marker fixed.

The first draft had one harmless overstatement: fixed-width simplicity is
true for `w<ell`, not `w=ell`, because every full-period window in one
ring has the same value.  That correction is incorporated in the current
theorem.  Since `h+1<ell`, it does not affect roots, owners, or immediate
uppers.

This audit does **not** promote the local adapter to a one-copy global ring
factor.  The exact remaining condition is a correlated selection of its
two companion ring states, cyclic filler orders, arbitrary-width tickets,
and serial capped ages.

## 1. Literal tensor check

Let the owner rank be `q`, the source-window width be `h`, and put

\[
                         s=q-h.
\]

Choose disjoint data

\[
 H,\quad a_0,a_1,a_2,\quad z,quad
 \lambda_1,\ldots,\lambda_{p-1},\quad
 \rho_1,\ldots,\rho_{p-1},                            \tag{1.1}
\]

where `|H|=s-1` and `p>=h`.  Ring `t` has invariant core

\[
                         K_t=H\cup\{a_t\}.             \tag{1.2}
\]

At its opened cut require cumulative profiles

\[
 \begin{aligned}
 L_i^t&=H\cup\{a_t,a_{t+1}\}
            \cup\{\lambda_1,\ldots,\lambda_{i-1}\},\\
 R_j^t&=H\cup\{a_t,z\}
            \cup\{\rho_1,\ldots,\rho_{j-1}\},
 \end{aligned}                                         \tag{1.3}
\]

for `1<=i,j<=p`.  These profiles are literal antipodal-ring collars:
the left terminal mover is `a_(t+1)`, the right initial mover is `z`,
and all other displayed movers are the ordered lambda/rho labels.

The old crossing value is

\[
 V_t(i,j)=H\cup\{z,a_t,a_{t+1}\}
    \cup\lambda[1,i)\cup\rho[1,j).                    \tag{1.4}
\]

Reconnect the left side of ring `t` to the right side of ring `t+1`.
Then

\[
 \boxed{
 N_t(i,j)=L_i^t\cup R_j^{t+1}=V_t(i,j).}              \tag{1.5}
\]

This is pointwise equality, not only multiset equality.  Disjointness in
(1.1) gives

\[
                         |V_t(i,j)|=q-h+i+j.            \tag{1.6}
\]

Consequently crossing widths `h-1,h,h+1` have ranks `q-1,q,q+1` and are
all transported exactly.  Taking `p=h` protects every split of all three
of these widths.  The equal-period construction in the main theorem uses
the entire common moving order and obtains (1.5) through the full period;
the mixed-period construction asserts only the local range through
`h+1`.

## 2. One-copy resources and minimal arity

For a fixed address `(i,j)`, the active signatures of the three values
in (1.4) are

\[
          \{a_0,a_1\},\quad\{a_1,a_2\},\quad
          \{a_2,a_0\}.                                \tag{2.1}
\]

They are distinct.  At a fixed width, the two ordered prefix lengths
recover `(i,j)`, so different addresses are also distinct.  Hence the
root, owner, and immediate-upper rows remain one-copy.

At the extreme owner split let

\[
 S=H\cup\{z,\rho_1,\ldots,\rho_{h-2}\}.               \tag{2.2}
\]

Then `|S|=q-2`, the three roots are `Q_t=S+a_t`, and the three owners are

\[
                         O_t=S+a_t+a_{t+1}.             \tag{2.3}
\]

Before the splice `Q_t` is attached to `O_t`; afterwards it is attached
to the other incident owner.  These are the two alternating matchings of
the Boolean incidence `C6`.  This confirms directly that the adapter is a
nontrivial owner/root factor trade even though every owner value is fixed.

Three components are minimal in this masked one-copy class.  With only
two cores `H+a_0,H+a_1`, each core must use the other label as its masking
terminal mover.  The two old tensors then have the same active signature
`{a_0,a_1}` at every common address and collide on their root/owner
resources.  Equivalently, a nontrivial two-component factor trade would
require a `C4` in the Boolean incidence graph, which does not exist.

## 3. Exact core exchange and serial state

Write one full ring partition as

\[
                         (K,F,U;x),                    \tag{3.1}
\]

where `x in F` is the terminal marker.  Choose

\[
                         u\in K,\qquad y\in U,          \tag{3.2}
\]

put `H=K-u`, `G=F-x`, and `Z=U-y`, and use the three input partitions

\[
 \begin{array}{c|c|c}
 K&F&U\\ \hline
 H+u&G+x&Z+y\\
 H+x&G+y&Z+u\\
 H+y&G+u&Z+x.
 \end{array}                                           \tag{3.3}
\]

Reading the three output seams from their new right-core sides gives

\[
 \begin{array}{c|c|c|c}
 K'&F'&U'&\text{terminal marker}\\ \hline
 H+x&G+u&Z+y&u\\
 H+y&G+x&Z+u&x\\
 H+u&G+y&Z+x&y.
 \end{array}                                           \tag{3.4}
\]

Thus the three possible continuation seams swap respectively

\[
                  K\leftrightarrow F,qquad
                  K\leftrightarrow U,qquad
                  F\leftrightarrow U.                 \tag{3.5}
\]

The middle row of (3.4) is exactly (0.1).  In particular, the auxiliary
label is not arbitrary: for a frozen input ring it must come from its
unused set.  At the two near-maximal periods this menu has size one or
two.

The regenerated seam has the same cumulative-profile form (1.3).  Hence
one of the three seams may be used as the shared collar of the next port;
the other two become internal seams of the fused component.  For one
port, (3.4) is the exact three-bin transposition projection and shows that
there is no congruence obstruction in the *unrestricted* partition-state
graph.

This does **not** prove full physical serial connectivity.  Under reuse of
one regenerated full-period collar, the nonterminal ordered filler bank

\[
                         G=F-\{\text{terminal marker}\}                 \tag{3.6}
\]

is invariant in all three rows of (3.4).  Changing `G` requires a new cut,
a filler-changing port, or retreat to the shorter mixed collar together
with independently protected long witnesses.  The full-tensor filler
fibre contains only polynomially many near-maximal ring states, so
exponentially many fibres are needed for the whole owner shore.  Cyclic
order, filler fibre, named tickets, and capped-age feasibility therefore
remain literal state coordinates; none is erased by the abstract
three-bin projection.

## 4. Topology and residence check

The tail permutation `t -> t+1` is a three-cycle, so it joins three input
cycles into one and inserts no source position.

In the equal-period model, write the moving sets as

\[
                 F_t=G\cup\{a_{t+1}\},                \tag{4.1}
\]

and leave `a_(t+2)` unused.  Every `g in G` occurs at the same phase in
the three consecutive blocks; its source occurrences are `ell` positions
apart, so its owner run/gap pair is `(h,ell-h)`.  A coordinate `a_t` is
the terminal mover of block `t-1`, is core throughout block `t`, and is
unused in block `t+1`.  Its source-positive and source-zero blocks have
lengths `ell+1` and `2ell-1`; after width-`h` union they give owner run and
gap

\[
                         (\ell+h,,2\ell-h).            \tag{4.2}
\]

Both entries are at least `h` when `ell>=2h`.  Common-core coordinates
are constant positive and common-unused coordinates constant zero.  This
proves one-port biresidence exactly.

Serial application is safe only when the designated collars retain the
same capped-age inequalities.  Partition-state connectivity alone does
not prove this, which is why the global theorem must carry cyclic order
and capped ages as literal state.

## 5. Exact remaining global gate

The local core-change obstruction is closed.  A global
`B(k)+O(1)` implication still requires a one-copy decorated ring
cover-down whose selected states contain a loose tree of compatible
masked triangles.  For every incident role it must jointly provide

\[
                         u\in K,quad x\in F,quad y\in U,               \tag{5.1}
\]

the two companion partitions in (3.3), a common cyclic filler order, and
all named occurrence tickets.  The selected cuts must also retain every
arbitrary-width witness not covered by (1.5) and pass serial capped ages.

Thus the result changes the frontier from

\[
 \text{construct a zero-charge core adapter}
\]

to

\[
 \boxed{\text{lift a large masked-triangle loose tree into the selected
 one-copy decorated ring factor}.}
\]

No additive sidecar is intrinsic to the adapter itself.  Any sidecar in a
global use comes only from nonlocal tickets or failed state/linkage
coverage, not from source length, roots, owners, or immediate uppers.
