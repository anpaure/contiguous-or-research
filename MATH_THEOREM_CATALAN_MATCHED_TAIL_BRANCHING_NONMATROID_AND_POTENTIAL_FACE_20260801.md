# Matched tails remove the lower row, but the remaining branching selector is not a matroid

**Date:** 2026-08-01  
**Lane:** protected Catalan forest / fixed perfect class  
**Status:** exact negative answer to the proposed branching-matroid collapse;
exact positive Rado face under a common strict potential.  No protected
Catalan forest or connector tree is constructed.

## 0. Outcome

Fix a perfect incidence matching

\[
 M_0:{\Omega\choose m-1}\longrightarrow {\Omega\choose m},
 \qquad I\subset M_0(I),\qquad |\Omega|=2m-1.                 \tag{0.1}
\]

For an upper colour \(R\in{\Omega\choose m+1}\), choose a tail
\(X\subset R\), put \(I=M_0^{-1}(X)\), and require the Johnson edge
\(X\to Y\) to have lower colour \(I\).  This restriction has one genuine
benefit:

\[
 \boxed{\text{distinct tails imply distinct lower colours}.}             \tag{0.2}
\]

It does **not** combine head injectivity and acyclicity into one branching
matroid.  In fact:

1. after \((R,X)\) is fixed, the head \(Y\) is unique, so the restriction
   creates no residual local menu;
2. sets of arcs with distinct heads and no directed cycle are the
   intersection of an incoming partition matroid and a graphic matroid,
   and are not a matroid;
3. this exchange failure occurs inside the Boolean Johnson host for every
   \(m\ge14\), with all thirteen upper colours and all thirteen lower
   colours distinct;
4. contracting a disjoint protected reset path does not remove the
   obstruction.

There is one exact positive face.  If all candidates increase one common
potential, acyclicity is automatic.  After tails have also been fixed and
made distinct, the remaining safety row is just the head partition matroid,
so ordinary Rado applies.  But with the matched-tail restriction every
upper-colour family is then a singleton.  If the tails are allowed to vary,
tail capacity reappears as a second crossing partition row.  Thus the
proposed restriction relocates the correlation; it does not solve it.

## 1. The matched-tail candidate is unique

Let \(R\) have rank \(m+1\), let \(X\subset R\) have rank \(m\), and put

\[
 I=M_0^{-1}(X),\qquad X=I\mathbin{\dot\cup}\{a\},
 \qquad R=X\mathbin{\dot\cup}\{b\}.                         \tag{1.1}
\]

### Lemma 1.1 (singleton candidate fibre)

There is exactly one rank-\(m\) head \(Y\) such that

\[
 X\cap Y=I,\qquad X\cup Y=R.
\]

It is

\[
                         Y=I\cup\{b\}=R\setminus\{a\}.       \tag{1.2}
\]

#### Proof

The required intersection forces \(Y\) to contain \(I\) and not \(a\).
The required union forces it to contain the only element \(b\) of
\(R-X\).  Since \(|Y|=m\), this determines (1.2). \(\square\)

Consequently, choosing a tail injection

\[
 \tau:{\Omega\choose m+1}\longrightarrow{\Omega\choose m},
 \qquad \tau(R)\subset R                                      \tag{1.3}
\]

already determines every physical arc.  The remaining constraints are
properties of this one global choice of \(\tau\), not a second Rado choice
inside the fixed-tail fibres.

The rooted link is isomorphic to the physical owner arc.  Indeed, if
\(J=M_0^{-1}(Y)\), then contraction of the perfect class sends

\[
                         X\longrightarrow Y
 \quad\hbox{to}\quad I\longrightarrow J,                    \tag{1.4}
\]

and \(M_0\) is a vertex bijection between the two directed graphs.

## 2. Why the intended branching family is not a matroid

On a directed graph whose selected tails are distinct, let \({\cal B}\)
consist of the arc sets having distinct heads and no directed cycle.  Under
the degree bounds, an undirected cycle is automatically coherently directed,
so these are exactly directed linear forests.

It is sometimes tempting to call \({\cal B}\) a branching matroid.  This is
not the relevant matroid.  The family is

\[
  {\cal B}={\cal I}(M_{\rm in})\cap{\cal I}(M_{\rm gr}),       \tag{2.1}
\]

the intersection of the incoming-head partition matroid and the graphic
matroid.  It need not satisfy augmentation.

The following Boolean witness makes the failure literal.

## 3. A Boolean exchange obstruction with thirteen distinct colours

Assume \(m\ge14\).  Choose a set \(K\) of size \(m-2\), distinct elements

\[
 a,b,c,d,e,f,g,h,s_1,s_2,s_3,s_4,s_5\notin K,               \tag{3.1}
\]

and distinct \(k_1,\ldots,k_5\in K\).  These use \(m+11\le2m-1\)
coordinates; add unused coordinates to obtain \(\Omega\).

Make two Johnson squares

\[
\begin{array}{llll}
 V_0=Kac,&V_1=Kab,&V_2=Kbd,&V_3=Kcd,\\
 W_0=Keg,&W_1=Kef,&W_2=Kfh,&W_3=Kgh,
\end{array}                                                   \tag{3.2}
\]

where juxtaposition denotes disjoint union.  Also put

\[
\begin{array}{lll}
 P_1=(V_1-k_1)+s_1,&P_2=(V_2-k_2)+s_2,&P_3=(V_3-k_3)+s_3,\\
 P_4=(W_1-k_4)+s_4,&P_5=(W_2-k_5)+s_5.&
\end{array}                                                   \tag{3.3}
\]

Prescribe the following thirteen incidences of \(M_0\):

\[
\begin{array}{llll}
 K+a\mapsto V_0,&K+b\mapsto V_1,&K+d\mapsto V_2,&K+c\mapsto V_3,\\
 K+e\mapsto W_0,&K+f\mapsto W_1,&K+h\mapsto W_2,&K+g\mapsto W_3,
\end{array}                                                   \tag{3.4}
\]

and

\[
 V_1-k_1\mapsto P_1,\quad V_2-k_2\mapsto P_2,\quad
 V_3-k_3\mapsto P_3,\quad W_1-k_4\mapsto P_4,\quad
 W_2-k_5\mapsto P_5.                                        \tag{3.5}
\]

All lower endpoints and all middle endpoints in (3.4)--(3.5) are distinct,
so this is a matching of size thirteen.  Every matching of size at most
\(m-1\) in the middle-levels incidence graph extends to a perfect matching:
after deleting \(t\) prescribed endpoints on each shore, the sharp middle
shadow surplus is at least \(t\), and residual Hall survives.  Hence
(3.4)--(3.5) extend to a perfect \(M_0\).

Now define

\[
\begin{aligned}
 A={}&\{V_0\to V_1,V_1\to V_2,V_2\to V_3,
       W_0\to W_1,W_1\to W_2,W_2\to W_3\},                 \tag{3.6}\\
 B={}&\{V_3\to V_0,W_3\to W_0,
       P_1\to V_1,P_2\to V_2,P_3\to V_3,
       P_4\to W_1,P_5\to W_2\}.                           \tag{3.7}
\end{aligned}
\]

Every arrow has the matched-tail form of Section 1.  For example,
\(M_0(K+a)=V_0\), and the lower colour of \(V_0\to V_1\) is
\(K+a\).  Similarly the lower colour of \(P_i\to H_i\) is
\(P_i\cap H_i=H_i-k_i\), which is mapped to \(P_i\) in (3.5).

### Theorem 3.1 (literal nonmatroid obstruction)

Both \(A\) and \(B\) have distinct tails, distinct heads, distinct lower
colours, distinct upper colours, and acyclic underlying graphs.  Moreover,

\[
                         |A|=6<7=|B|,                         \tag{3.8}
\]

but

\[
                         A+e\notin{\cal B}
                         \qquad(e\in B-A).                   \tag{3.9}
\]

Therefore \({\cal B}\) is not the independent-set family of a matroid,
even on the matched-tail Boolean ground and even after restricting to
pairwise distinct upper-colour atoms.

#### Proof

The set \(A\) is the disjoint union of two directed three-edge paths.
The set \(B\) is a forest: its two square-closing edges and five pendant
edges lie in separate tree pieces.  Its seven heads are

\[
                 V_0,W_0,V_1,V_2,V_3,W_1,W_2,
\]

which are distinct.

The four upper colours on the first square are the four distinct sets

\[
 Kabc,\quad Kabd,\quad Kbcd,\quad Kacd,                     \tag{3.10}
\]

and the second square has the analogous four colours on \(e,f,g,h\).
The pendant colours are \(V_1+s_1,V_2+s_2,V_3+s_3,W_1+s_4,W_2+s_5\),
which are distinct from one another and from (3.10) because the \(s_i\)
are fresh.  The lower-colour assertion follows from the thirteen distinct
preimages in (3.4)--(3.5).

Adding \(V_3\to V_0\) to \(A\) closes the first four-cycle, and adding
\(W_3\to W_0\) closes the second.  Each pendant arrow in \(B\) has a head
already used by \(A\).  Thus every possible augmentation fails, proving
(3.9). \(\square\)

### Corollary 3.2 (protected contraction does not cure the axiom)

If a protected reset link path is vertex-disjoint from the thirteen owner
vertices above, contracting that path leaves the restrictions of \(A\) and
\(B\) unchanged.  Hence the same augmentation failure survives in the
contracted instance.

More generally, one may prescribe the protected predecessor matching and
(3.4)--(3.5) simultaneously whenever their total size is at most \(m-1\);
the same sharp-shadow extension argument supplies a common perfect class.
Thus the obstruction is compatible with a bounded or \(O(\sqrt m)\)
protected bank in sufficiently large dimension.  This does not say that
every fixed \(M_0\) contains the displayed witness; it disproves a uniform
branching-matroid reduction.

## 4. The exact positive Rado face

The preceding obstruction disappears if acyclicity is made automatic
*before* the transversal is selected.

### Theorem 4.1 (common-potential head Rado)

Let \(P_0\) be a protected forest.  Suppose that:

1. every residual upper colour \(R\) has a fixed distinct tail \(\tau(R)\);
2. every candidate arc, and every protected arc, strictly increases one
   common potential \(\phi\);
3. the matched-tail restriction \(M_0^{-1}(\tau(R))=	au(R)\cap Y\) holds;
4. any additional payload is hereditary/private and creates no further
   crossing resource row.

Then acyclicity and lower-colour injectivity are automatic.  The remaining
safety matroid is the partition matroid on physical heads.  A protected
upper-colour transversal exists exactly when

\[
 \left|\{Y:\ X\to Y\in\bigcup_{R\in S}{\cal E}_R\}
          \setminus H(P_0)\right|\ge |S|                    \tag{4.1}
\]

for every residual upper-colour family \(S\).

#### Proof

Distinct tails and bijectivity of \(M_0\) give distinct lower colours.
The strict potential forbids directed, hence undirected, cycles under the
degree bounds.  Head capacity is a partition matroid.  Rado's theorem in
that partition matroid, contracted by the protected heads, gives (4.1).
\(\square\)

For the literal restriction of Lemma 1.1, however, each fixed-tail menu
\({\cal E}_R\) contains at most one arc.  Then (4.1) merely checks that the
already determined heads are distinct.  It does not provide a mechanism
for choosing the tails.

If the tails are allowed to vary, the atom ground is

\[
 (R,X,Y),\qquad X\subset R,quad
 Y=R\setminus\bigl(X-M_0^{-1}(X)\bigr),                    \tag{4.2}
\]

and one must impose both tail and head capacities.  This is a three-partite
matching face (upper task, tail, head), not one partition matroid.  Boolean
shadow surplus proves the marginal upper-to-tail Hall system, but Theorem
3.1 shows that it cannot supply the missing correlated head/acyclic row by
an ordinary matroid rank inequality.

## 5. Consequence for the Catalan connector programme

The proposed collapse closes exactly one resource:

\[
                  \text{tail injection}\Longrightarrow
                  \text{lower-colour injection}.             \tag{5.1}
\]

The protected \(Q_0\) problem remains a correlated selector for

\[
 \boxed{\text{upper task}\;|\;\text{tail}\;|\;\text{head}
        \;|\;\text{graphic acyclicity}.}                     \tag{5.2}
\]

There are two proof-safe routes left:

1. construct a support or a common strict potential first, so graphic
   acyclicity is automatic, and then prove a genuinely aligned/private
   head--tail selector; or
2. retain the exact intersection of the tail partition, head partition and
   graphic matroid, and prove a Boolean-specific integral theorem rather
   than invoking Rado.

Even after \(Q_0\) is supplied, its \(\operatorname{Cat}_m\)-component
connector tree has the same outgoing-port, incoming-port and graphic
intersection.  It becomes Rado only on a corresponding common-potential or
private functional-port face.  Therefore no Catalan component-connector
theorem follows from the matched-tail restriction alone.

## 6. Corrected frontier

The exact immediate theorem is not a branching-matroid rank inequality.
It is:

> **Matched-tail protected support theorem.**  Construct, in correlation,
> an upper-exact atom set whose tails are distinct, whose matched heads are
> distinct, and whose arcs lie in one common-potential support containing
> the protected complete-reversal path; then construct a common-potential
> free-port connector support for its Catalan components.

On such a supplied support, both remaining selections reduce to ordinary
partition-matroid Rado/Hall.  Production of that support is still the
unproved Catalan-scale gate.
