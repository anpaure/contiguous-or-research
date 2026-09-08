# Close-packed octahedral trades: trace cocycles and strip holonomy

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

The exact multiseam trace ledger becomes linear after passing to the
order-\(q\) window graph.  A factor is a 1-cycle there, and its signed
trace vector is a label pushforward of that cycle.  This gives a precise
meaning to “interior defects cancel and only the boundary remains.”

For a chain or periodic strip of octahedral cells sharing the same three
rails, however, the component topology is controlled by one
\(S_3\)-holonomy.  Arbitrarily many local matching changes can alter the
number of components by at most two.  Thus a periodic three-rail tiling
may have a boundary-only trace defect, but it cannot accumulate joining
rank proportional to its number of seams.

More generally, an \(s\)-sheet strip changes component count by at most
\(s-1\).  If strips have protected longitudinal scale at least \(H\),
their total joining rank is \(O(W/H)\).  This is
\(o(W/\sqrt m)\) in the coefficient-one regime and cannot collapse the
product-SCD path count.  A surviving close-packed construction must be a
genuinely two-dimensional complex whose transverse sheet number grows and
whose trace cocycle vanishes globally; repeated use of one fixed
octahedral rail chain is ruled out.

No homological obstruction for every two-dimensional complex is proved.

## 1. Exact linearization by the window graph

Let \({\cal A}\) be the set of oriented Johnson edges, with compatibility
given by consecutive edges sharing their middle owner.  For fixed
\(q\ge1\), define the directed window graph \({\cal D}_q\):

* a vertex is a valid word of \(q-1\) consecutive oriented Johnson edges;
* an edge is a valid word

  \[
                         \omega=(e_1,\ldots,e_q),                 \tag{1.1}
  \]

  directed from its length-\((q-1)\) prefix to its
  length-\((q-1)\) suffix.

Give (1.1) the two literal labels

\[
 \lambda_q^-(\omega)=\bigcap_{i=1}^q\ell(e_i),\qquad
 \lambda_q^+(\omega)=\bigcup_{i=1}^q u(e_i),                     \tag{1.2}
\]

where \(\ell(XY)=X\cap Y\) and \(u(XY)=X\cup Y\).

For a directed path/cycle factor \(F\), let \(Z_q(F)\) be the integral
1-chain in \({\cal D}_q\) obtained by summing all its \(q\)-windows.
Let

\[
 \Lambda_q^\pm:C_1({\cal D}_q;\mathbb Z)
        \longrightarrow
        \mathbb Z^{\binom{[N]}{m\mp q}}                         \tag{1.3}
\]

send a window edge to the basis vector of its label.

### Theorem 1.1 (exact trace-chain identity)

For every factor,

\[
                         \mu_q^\pm(F)=\Lambda_q^\pm Z_q(F).      \tag{1.4}
\]

Consequently, for two factors \(F,F'\),

\[
 \boxed{\;
 \mu_q^\pm(F')-\mu_q^\pm(F)
   =\Lambda_q^\pm\bigl(Z_q(F')-Z_q(F)\bigr).\;}                  \tag{1.5}
\]

If the factor components are cycles, \(\partial Z_q(F)=0\).  If they are
paths, \(\partial Z_q(F)\) is supported only on their two
length-\((q-1)\) endpoint contexts.

#### Proof

Equation (1.2) is the meet/join word identity.  Each occurrence of a
literal target is one edge of the window graph carrying that label, so
summing gives (1.4).  Boundary cancellation is the usual cancellation of
successive prefix/suffix contexts along a word. \(\square\)

Thus a collection of local replacements has boundary-only defect exactly
when the label pushforward of its total window-chain difference is
supported on the external context boundary.  Pairwise cancellation at
depth one is only the projection of (1.5) to \({\cal D}_1\); it does not
imply cancellation in \({\cal D}_q\).

For all depths at once, use the product map

\[
                         \Lambda_{\le H}
             =\bigoplus_{q\le H,\ \pm}\Lambda_q^\pm.             \tag{1.6}
\]

The exact close-packed problem is to construct a large factor trade
whose window-chain difference lies in \(\ker\Lambda_{\le H}\), or differs
from that kernel by a chain supported on only \(o(W)\) external windows.

## 2. A layered octahedral strip

Let \(L\ge1\).  At each cyclic layer \(t\in\mathbb Z/L\mathbb Z\), take
three ports \((t,i)\), \(i\in\{1,2,3\}\).  A matching between layers
\(t\) and \(t+1\) is a permutation

\[
                         \pi_t\in{\mathfrak S}_3,\qquad
        (t,i)\longrightarrow(t+1,\pi_t(i)).                      \tag{2.1}
\]

The two octahedral resolutions are the two \(3\)-cycles in
\({\mathfrak S}_3\).  Allowing either resolution at every layer is the
most favorable abstract model of a close-packed chain of the lifted
trades: it forgets all literal-owner and collar restrictions but retains
the complete component topology.

Put

\[
                         \Pi=\pi_{L-1}\cdots\pi_1\pi_0.           \tag{2.2}
\]

### Theorem 2.1 (strip holonomy)

The number of directed factor cycles in the strip is exactly

\[
                         c(\Pi),                                 \tag{2.3}
\]

the number of cycles of the monodromy permutation.  Therefore any two
choices of the \(L\) octahedral resolutions differ in component count by
at most two, independently of \(L\).

#### Proof

Starting at \((0,i)\) and traversing one full longitudinal period returns
to layer zero at \((0,\Pi(i))\).  Factor components are precisely the
orbits of \(\Pi\).  A permutation of three points has between one and
three cycles. \(\square\)

This theorem answers the proposed periodic-chain escape negatively.
Even if the interior trace cocycles in (1.5) cancel perfectly and only
\(O(H)\) boundary windows remain, the joining rank of the entire
three-rail strip is \(O(1)\), not \(\Theta(L)\).

There is also an exact gauge interpretation.  Relabel the three ports in
layer \(t\) by \(g_t\in{\mathfrak S}_3\).  The matchings transform as

\[
                         \pi_t'
               =g_{t+1}\pi_tg_t^{-1}.                           \tag{2.4}
\]

On a periodic strip \(g_L=g_0\), so

\[
                         \Pi'=g_0\Pi g_0^{-1}.                   \tag{2.5}
\]

Every pure interior gauge deformation preserves component count exactly.
Only the holonomy class can change it, and that class carries at most two
units of joining rank.

## 3. The \(s\)-sheet and packing bounds

The preceding argument is not special to three sheets.

### Corollary 3.1 (finite-sheet ceiling)

For an \(s\)-sheet layered strip with permutation matchings
\(\pi_t\in{\mathfrak S}_s\), the number of components is the number of
cycles of the monodromy.  Hence the joining rank of an arbitrary
close-packed sequence of local matching changes is at most \(s-1\).

Suppose a construction is a disjoint union of strips \(j\), with
longitudinal owner length \(L_j\ge H\) and transverse widths \(s_j\).
Then

\[
                         \sum_jL_js_j\le W
 \quad\Longrightarrow\quad
                         \sum_j r_{{\rm join},j}
        \le\sum_j(s_j-1)\le {W\over H}.                         \tag{3.1}
\]

In the regime \(H/\sqrt m\to\infty\), this is
\(o(W/\sqrt m)\).

#### Proof

The monodromy proof of Theorem 2.1 works verbatim in
\({\mathfrak S}_s\).  A permutation of \(s\) points has between one and
\(s\) cycles.  The owner and joining inequalities then give (3.1).
\(\square\)

Thus sharing rails removes the factor \(H\) from the *trace-boundary*
ledger but not from the *topological-capacity* ledger: one longitudinal
strip has only its transverse sheet count available as joining rank.

## 4. What a two-dimensional escape must do

There is a second exact boundary obstruction before looking at traces.

### Proposition 4.1 (literal edge-boundary rank bound)

Let \(F,F'\) be two 2-factors on the same owner set and put

\[
                         k=|E(F')\setminus E(F)|
                          =|E(F)\setminus E(F')|.                 \tag{4.1}
\]

Then

\[
                         |c(F')-c(F)|\le k.                       \tag{4.2}
\]

Consequently, if a 2-chain of octahedral cells cancels all its literal
interior edge derivatives and leaves only \(b\) new boundary edges, its
joining rank is at most \(b\).  A periodic cell 2-cycle whose literal
edge boundary is zero returns the identical factor and has zero joining
rank.

#### Proof

Put \(G=F\cap F'\).  Deleting the \(k\) old-only edges cannot decrease
component count and increases it by at most \(k\), so

\[
                         c(F)\le c(G)\le c(F)+k.
\]

Adding the \(k\) new-only edges to \(G\) cannot increase component count,
whence \(c(F')\le c(G)\le c(F)+k\).  Interchanging \(F,F'\) gives the
reverse inequality and proves (4.2). \(\square\)

Thus literal cellular cancellation cannot simultaneously leave a small
boundary and produce extensive joining rank.  The only possible
two-dimensional escape is subtler: the **edge** derivative must remain
extensive while its **trace** image under every \(\Lambda_q^\pm\) cancels.
In other words, one needs an extensive nonzero class in the kernel of the
trace map, not an ordinary cellular 2-cycle.

A genuine escape cannot decompose into bounded-sheet longitudinal
strips.  It must use a two-dimensional complex in which octahedral cells
move between different triples of sheets, so that the transverse
component space itself grows.

For such a complex \({\cal K}\), define its exact protected trace cocycle

\[
 {\mathfrak d}_{\le H}({\cal K})
   =\Lambda_{\le H}\bigl(Z_{\le H}(F_{\rm new})
                         -Z_{\le H}(F_{\rm old})\bigr).          \tag{4.3}
\]

Here \(Z_{\le H}=\bigoplus_{q\le H}Z_q\).

The desired theorem would require simultaneously

\[
                         \|{\mathfrak d}_{\le H}({\cal K})\|_1
                                  =o(W)                          \tag{4.4}
\]

and joining rank \(\Theta(W/\sqrt m)\).  Equation (1.5) shows that
“interior cancellation” means literal cancellation of the lifted
window-chain, not merely cancellation of direction counts or of
depth-one octahedral boundaries.

There are two possible outcomes for a proposed periodic 2-complex.

1. If its local cells are related by layer gauges as in (2.4), its
   topology reduces to boundary holonomy and cannot accumulate extensive
   joining rank.
2. If it has extensive joining rank, it represents a non-gauge
   homology class.  One must then prove that this class lies in
   \(\ker\Lambda_{\le H}\).  No such literal both-sign class is presently
   known.

The fixed-sheet theorem is a quantitative obstruction, not a universal
homological no-go.  A two-dimensional complex could in principle have an
extensive kernel class.  Finding one is now the exact close-packed
octahedral target.

## 5. Audited boundary

Proved:

* exact linearization of every signed depth through the window graph;
* exact \(S_3\) holonomy for an arbitrary periodic octahedral rail chain;
* \(O(1)\), rather than extensive, joining rank on three shared rails;
* the \(W/H\) joining ceiling for disjoint finite-sheet strips.

Not proved:

* that every literal octahedral 2-complex decomposes into such strips;
* injectivity of \(\Lambda_{\le H}\) on every non-gauge homology class;
* an explicit extensive class in \(\ker\Lambda_{\le H}\).

Therefore the simple periodic-chain escape is closed.  The only
remaining close-packed version is a growing-sheet two-dimensional trace
cocycle.
