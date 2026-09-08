# Master-handoff rigor repair: Appendices H.1, H.11, and H.15

**Purpose.**  This note supplies the indexed definitions suppressed in the
minified version of Appendix H.  It makes the local/remote decomposition an
exact finite identity and proves the two estimates quoted in (H.11.8) and
(H.15.0.1).  It is written as insertion/replacement text; it does not use a
checker or any external mathematical premise.

**Insertion guidance.**

1. Near the first use of falling factorials in the handoff, insert
   \[
      (n)_a=n(n-1)\cdots(n-a+1),\qquad (n)_0=1.
   \]
2. Insert Block H-A immediately after current equation (H.1.9).
3. In H.11, replace the prose beginning “Before edge orientation is
   forgotten” through (H.11.8) by Block H-B.
4. In H.15.3, replace the definitions of
   \(\mathcal A_{\rm rem}(t)\) and \(R_s(t)\), and the paragraph proving
   (H.15.3.3)--(H.15.3.4), by Block H-C.  The pointwise current theorem
   H.15.2.1 may remain unchanged.

The notation below continues the definitions of H.1: \(b=2r+1\),
\(X,E_0,\psi_t,\mathcal P_t,B_r(t)\), the boundary-placement set
\(\mathcal B_t\), its sign \(\varepsilon(z)\), and the signed profile
\(\omega_x(t)\).

## Block H-A: the exact signed blocker current

For an edge set \(J\subseteq E(\widetilde B_r)\), define

\[
 \mathfrak I_{s,t}(J)=\frac1{|\mathcal B_t|}
 \sum_{z\in\mathcal B_t}\varepsilon(z)
 \sum_{\substack{S\text{ tagged}\\ |\underline S|=s}}
 H_j(z\underline S)\,\deg_t(S,J),
 \qquad s\in\{r,r-1\}.                                      \tag{H-A.1}
\]

Here a placement in \(\mathcal B_t\) is completed to a permutation only
to give meaning to \(zU=\{z(u):u\in U\}\).  The summand depends solely on
the placed distinguished labels, so (H-A.1) is independent of the chosen
completion.

Finite inclusion--exclusion in (H.1.4), followed by interchange of two
finite sums, gives the literal identity

\[
 \boxed{\omega_{Z_s}(t)=
 \sum_{J\subseteq E(B_r(t))}(-1)^{|J|}\mathfrak I_{s,t}(J).} \tag{H-A.2}
\]

This formula fixes all multiplicities: every blocker set is an ordinary
edge subset and occurs once, with its inclusion--exclusion sign.

There is a useful current interpretation.  For fixed \(t,z,J\), interchange
the root-target and configuration sums in the numerator of (H-A.1):

\[
 \sum_S H_j(z\underline S)\deg_t(S,J)
 =\sum_{w:E(w)\supseteq\psi_t^{-1}(J)}
   \sum_{a=1}^{b-1}H_j\!\left(zI_s^w(a)\right).             \tag{H-A.3}
\]

Thus the numerator is a shore current of exactly the form used in
H.15.1, after relabelling the distinguished pairs by \(z\), and then
multiplied by the sign \(\varepsilon(z)\), whose modulus is one.  It
follows directly from H.15.2.1 that

\[
 |\mathfrak I_{s,t}(J)|\le2r\deg_t(J),\qquad
 |\mathfrak I_{r,t}(J)-\mathfrak I_{r-1,t}(J)|
 \le2j\deg_t(J),                                         \tag{H-A.4}
\]

where \(\deg_t(J)=|\{w:E(w)\supseteq\psi_t^{-1}(J)\}|\).
The second inequality is valid because the same \(z,J,w\) are coupled on
the two shores before averaging.

The two displayed adjacent position pairs in the definition of
\(\mathcal B_t\) are the **event edges**.  After applying \(\psi_t\), their
two cut roots are

\[
                         p=0,\qquad q=5.                    \tag{H-A.5}
\]

If \(p\notin V(J)\), transpose the two positions of the first event edge.
This fixes every blocker target in \(J\), pairs the root targets, and
reverses exactly one factor in the harmonic product.  Hence
\(\mathfrak I_{s,t}(J)=0\).  The same argument at the second event edge
applies when \(q\notin V(J)\).  Therefore

\[
 \boxed{\mathfrak I_{s,t}(J)=0
       \quad\text{unless}\quad\{0,5\}\subseteq V(J).}      \tag{H-A.6}
\]

This is the precise version of “the boundary-event profile vanishes unless
the blocker set is incident with both roots.”

## Block H-B: indexed local atoms and supplier totals

Use the sixteen supports \(\mathscr V\) and the six path supports
\(\mathscr Q_V\) listed in (H.11.1)--(H.11.2).  Define the complete signed
local multiset

\[
 \mathscr A_{\rm loc}^{\circ}=
 \{(+1,M(V)):V\in\mathscr V\}
 \;\dot\cup\;
 \{(-1,P(V)):V\in\mathscr Q_V\}.                          \tag{H-B.1}
\]

It has sixteen positive matching entries and six negative path entries.
The sign in (H-B.1) is exactly \((-1)^{|J|}\), since a matching has two
edges and a path has three.  At puncture shift \(t\), retain only entries
whose edge set avoids \(\mathcal P_t\):

\[
 \mathscr A_{\rm loc}(t)=
 \{(\eta,J)\in\mathscr A_{\rm loc}^{\circ}:
                         J\cap\mathcal P_t=\varnothing\}.   \tag{H-B.2}
\]

The local profile is now the explicit finite sum

\[
 \boxed{L_{s,j}(t)=
   \sum_{(\eta,J)\in\mathscr A_{\rm loc}(t)}
             \eta\,\mathfrak I_{s,t}(J).}                  \tag{H-B.3}
\]

This equals \(\omega_{\mathcal L_{s,t}}(t)\) in (H.11.3), by linearity.
The complete, unpunctured sum

\[
 \Omega_{s,j}=
   \sum_{(\eta,J)\in\mathscr A_{\rm loc}^{\circ}}
             \eta\,\mathfrak I^{\circ}_{s,t}(J)           \tag{H-B.4}
\]

is independent of \(t\).  Here \(\mathfrak I^{\circ}\) is defined by
(H-A.1) using the full graph \(\widetilde B_r\), before requiring
\(J\cap\mathcal P_t=\varnothing\).  Translation of cut positions is a
bijection of placements, target tuples, and label assignments, proving the
independence.

We next make the supplier classification literal.  A tagged central target
\(T=(\sigma,I_{s_\sigma}(u))\), \(s_M=r,s_L=r-1\), has an oriented boundary
edge with

\[
 \operatorname{st}_t(T)=-2(u-t),\qquad
 \operatorname{en}_t(T)=-2(u+s_\sigma-t)\pmod b.           \tag{H-B.5}
\]

For every entry \((\eta,J)\) in (H-B.1), exactly one edge of \(J\) is
incident with each of the roots \(0,5\): this is immediate for a matching,
and in each of the six paths the roots are its endpoints.  That unique edge
is the **supplier** at the root.  Give it type \(S\) when the root is its
start endpoint in (H-B.5), and type \(E\) when the root is its end endpoint.
For \(\alpha,\beta\in\{S,E\}\), define

\[
 F_{s,\alpha\beta}=
 \sum_{\substack{(\eta,J)\in\mathscr A_{\rm loc}^{\circ}\\
        \text{supplier types at }(0,5)=(\alpha,\beta)}}
       \eta\,\mathfrak I^{\circ}_{s,t}(J).                 \tag{H-B.6}
\]

Equations (H-B.4)--(H-B.6) give

\[
 \Omega_{s,j}=F_{s,SS}+F_{s,SE}+F_{s,ES}+F_{s,EE}.          \tag{H-B.7}
\]

For clarity about the sign under reflection, after multiplication by
\(\varepsilon(z)\) the harmonic factor is

\[
 \varepsilon(z)H_j(z\underline S)=
 \prod_{i=1}^j
 \bigl(\mathbf1_{\{u_i\in\underline S\}}-
       \mathbf1_{\{v_i\in\underline S\}}\bigr),           \tag{H-B.8}
\]

where \(u_i\) and \(v_i\) are respectively the inside and outside
positions of event pair \(i\).  Thus it depends only on the oriented split,
not on the names of the two distinguished labels.  The reflection
\(a\mapsto5-a\) bijects the local entries and their placement sums,
preserves Venn-cell factorials and the sign \((-1)^{|J|}\), and reverses
the start/end role at both suppliers while exchanging the two roots.
Consequently

\[
                              F_{s,SS}=F_{s,EE}.             \tag{H-B.9}
\]

At \(t=0\),
\(\mathcal P_0=\{\{0,1\},\{0,3\}\}\) consists precisely of the two
possible start suppliers at root \(0\).  Since a local entry has a unique
supplier there, no entry contains both punctured edges, and hence

\[
 \Omega_{s,j}-L_{s,j}(0)=F_{s,SS}+F_{s,SE}.                 \tag{H-B.10}
\]

Since \(2\ell\equiv5\pmod b\), at \(t=\ell=r+3\) the two punctured edges
are \(\{5,6\},\{5,8\}\), the two possible start suppliers at root \(5\):

\[
 \Omega_{s,j}-L_{s,j}(\ell)=F_{s,SS}+F_{s,ES}.              \tag{H-B.11}
\]

At \(t=3\), the punctured edges \(\{6,7\},\{6,9\}\) occur in no local
entry listed in (H.11.1), so

\[
                              L_{s,j}(3)=\Omega_{s,j}.       \tag{H-B.12}
\]

Adding (H-B.10)--(H-B.11) and using (H-B.7)--(H-B.9) gives

\[
 \boxed{L_{s,j}(0)+L_{s,j}(\ell)=L_{s,j}(3).}               \tag{H-B.13}
\]

This proves the local identity without any undefined supplier total.

## Block H-C: exact remote family, decomposition, and mass bound

Define the complete indexed blocker family surviving the puncture by

\[
 \mathscr A_{\rm all}(t)=
 \left\{\bigl((-1)^{|J|},J\bigr):
 J\subseteq E(B_r(t)),\ \{0,5\}\subseteq V(J)\right\}.     \tag{H-C.1}
\]

Regard \(\mathscr A_{\rm loc}(t)\) from (H-B.2) as the corresponding
submultiset of (H-C.1), and put

\[
 \mathscr A_{\rm rem}(t)=
       \mathscr A_{\rm all}(t)\setminus
       \mathscr A_{\rm loc}(t),                           \tag{H-C.2}
\]

\[
 \boxed{R_{s,j}(t)=
 \sum_{(\eta,J)\in\mathscr A_{\rm rem}(t)}
                  \eta\,\mathfrak I_{s,t}(J).}             \tag{H-C.3}
\]

The subtraction in (H-C.2) is literal: on each of the ten matching-only
supports it removes the matching; on each of the six path supports it
removes both the endpoint matching and the full path.  There are no other
four-vertex edge subsets incident with both roots.  Indeed the two roots
have disjoint neighbour sets; choosing one neighbour of each gives the
sixteen supports in (H.11.1).  On ten supports the two supplier edges are
the only induced edges.  On the remaining six the sole additional edge is
the connector, so the only edge subsets incident with all four vertices
are the matching and the full path.

By (H-A.2) and the root cancellation (H-A.6), every surviving
inclusion--exclusion term belongs to exactly one of (H-B.2) and (H-C.2).
Therefore

\[
 \boxed{\omega_{Z_s}(t)=L_{s,j}(t)+R_{s,j}(t).}              \tag{H-C.4}
\]

It remains to bound the unsigned remote mass

\[
 \mathcal M_{\rm rem}(t)=
       \sum_{(\eta,J)\in\mathscr A_{\rm rem}(t)}\deg_t(J).
                                                                    \tag{H-C.5}
\]

For every such \(J\), the boundary-codegree theorem gives

\[
 \deg_t(J)\le D_M C_0^{|J|}r^{\,2-|V(J)|}.                \tag{H-C.6}
\]

Here is the complete summation.  Decompose \(J\) into connected
components.  Its rooted part is the union of the one or two components
meeting \(0\) or \(5\).  A maximum-degree-four exploration from a fixed
root has at most \(A_0^m\) connected \(m\)-edge shapes.  If one rooted
component contains both roots, then a four-vertex possibility is one of
the six local paths; every nonlocal possibility has at least five vertices.
If the roots lie in separate components, the only four-vertex possibility
is a pair of disjoint supplier edges, one of the ten local matchings;
otherwise the rooted part again has at least five vertices.  Together with
\(m\le2(v-1)\), this shows that the total weight in (H-C.6) of a nonlocal
rooted part is \(O(D_Mr^{-3})\): the finitely many small \(m\) have
\(v\ge5\), while the remaining terms are bounded by a geometric series in
\(A_0C_0/\sqrt r\).

A connected component meeting neither root, with \(m\) edges and \(v\)
vertices, has at most \(bA_0^m\) placements.  Its activity after removal of
the common factor \(D_Mr^2\) is
\(C_0^m r^{-v}\).  The one-edge total is \(O(1/r)\); the two- and
three-edge totals are smaller by triangle-freeness; and
\(m\le2(v-1)\) makes all \(m\ge4\) terms a convergent geometric tail.
Thus the total unrooted connected activity is \(O(1/r)\), and allowing any
unordered family of such components multiplies a rooted contribution by
at most \(\exp(O(1/r))\).  Finally, if the rooted part is one of the local
four-vertex entries but \(J\) is remote because it has an additional
component, the nonempty additional family contributes the extra factor
\(O(1/r)\).  Hence, uniformly in \(t\),

\[
 \boxed{\mathcal M_{\rm rem}(t)\le C D_Mr^{-3}.}             \tag{H-C.7}
\]

Apply (H-A.4) termwise to (H-C.3) and then (H-C.7):

\[
 \boxed{|R_{s,j}(t)|\le C D_Mr^{-2},\qquad
 |R_{r,j}(t)-R_{r-1,j}(t)|\le CjD_Mr^{-3}.}                 \tag{H-C.8}
\]

Equations (H-C.4) and (H-C.8) are precisely the rigorously indexed content
of current (H.11.8) and (H.15.0.1).  They prove only the stated partial
Gate-B estimates; no positive all-depth cover follows from them.
